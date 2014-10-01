__author__ = 'quek'

from collections import OrderedDict
import re
from operator import itemgetter
import json



def write_entry(entry_dict, filehandle):
    js_string = json.dumps(entry_dict, sort_keys=False)
    filehandle.write('%s\n' % js_string)








def parseAC(line, source):
    line = re.split('^AC', line)
    Id = line[1]
    Ids = Id.split(';')
    Ids = [x.strip() for x in Ids if x is not '']
    if len(Ids) == 1:
        return OrderedDict ([('_id', Ids[0]),
                             ('ID', ''),
                             ('source', source),
                             ('PMID',[])
                            ])


    return OrderedDict([('_id', Ids[0]),
                        ('ID', ''),
                        ('source', source),
                        ('PMID', []),
                        ('sec_acc', Ids[1:])
                       ])

def parseAC_2ndline(line):
    line = re.split('^AC', line)
    Id = line[1]
    Ids = Id.split(';')
    Ids = [x.strip() for x in Ids if x is not '']
    return Ids

def parsePMID(line):
    PMID = re.search('PubMed=(\d+);', line).group(1)
    return int(PMID)

def parseID(line):
    return re.match('ID\s{3}(\w+)',line).group(1)

def parseENS(line):
    ENS = re.split('DR|\.|;', line)
    ENS = ENS[2:]
    ENS = [x.strip() for x in ENS if x is not '' ]
    if len(ENS) > 3:
        isoform = ENS.pop()
        isoform = re.search('-(\d+)]', isoform).group(1)
        isoform = int(isoform)
        return OrderedDict([('iso', isoform),
                            ('ENS', ENS)])
    return OrderedDict([('iso', 1), ('ENS', ENS)])

def mainParser(mockfile, source, filehandle):
    entry_list = []
    entry_dict = None
    previous_line = ''
    with open(mockfile) as f:
        for line in f:
            line = line.strip()
            if line.startswith('ID'):
                if entry_dict:
                    #entry_list.append(entry_dict)
                    write_entry(entry_dict, filehandle)
                current_id = parseID(line)

            elif line.startswith('AC'):
                if previous_line.startswith('AC'):
                    entry_dict['sec_acc'].extend(parseAC_2ndline(line))
                else:
                    entry_dict = parseAC(line, source)
                    entry_dict['ID'] = current_id
            elif line.startswith('DR'):
                if 'gene' in entry_dict:
                    entry_dict['gene'].append(parseENS(line))
                    entry_dict['gene'] = sorted(entry_dict['gene'], key=itemgetter('iso'))
                else:
                    entry_dict['gene'] = []
                    entry_dict['gene'].append(parseENS(line))

            elif line.startswith('RX'):
                entry_dict['PMID'].append(parsePMID(line))

            previous_line = line

        #entry_list.append(entry_dict)
        write_entry(entry_dict ,filehandle)

        print entry_list
    return entry_list

if __name__ == '__main__':
    with open('uniprot_out/swiss.json', 'w+') as f:
        mainParser('gene_sprot', 'swiss', f)