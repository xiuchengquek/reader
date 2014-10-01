__author__ = 'quek'

from collections import Counter, defaultdict, OrderedDict
import json


def Printer(file, current_id, counter, term):
    fh_out = open(file, 'a+')

    for key, value in term.iteritems():
        count = counter[key]
        term_type = term[key]
        collated_dict = OrderedDict([('PMID', current_id), ('type', term_type), ('term', key), ('count', count)])
        fh_out.write('%s\n' % json.dumps(collated_dict))


def Reader(inputfile, linebreak):
    file_count = 0
    line_counter = 1
    outfile = "outdir/file_%i" % file_count
    fh_out = open(outfile, 'a+')
    termCounter = defaultdict()
    termDict = {}

    with open(inputfile) as f:
        for lines in f.readlines():
            lines = lines.strip()
            fields = lines.split('\t')
            current_id = fields[0]
            termDict[current_id[4]] = current_id[3]
            termCounter[current_id[-1]]

            if previous_id != current_id:
                Printer(outfile, previous_id, termCounter, termDict)

            if line_counter > linebreak:
                if previous_id != current_id:
                    file_count += 1
                    print 'Completed Approx %i' % ((file_count + 1) * line_counter + 1)
                    outfile = "outdir/file_%i" % file_count
                    fh_out = open(outfile, 'a+')
                    line_counter = 1
            line_counter += 1
            previous_id = current_id
    fh_out.close()


if __name__ == '__main__':
    Reader('mocktest.txt', 10)