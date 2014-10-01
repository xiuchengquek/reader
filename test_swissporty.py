__author__ = 'quek'

import unittest

from swissporty import mainParser, parseAC, parsePMID,parseENS, parseID
import json
from collections import OrderedDict








from mock import MagicMock, patch


def side_effect(value, fh):
    return value


m = MagicMock(side_effect=side_effect)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.singleMock = 'resources/singleMock.txt'
        self.mockfile = 'resources/mockEntry.txt'
        self.mockout = 'resources/mockout.json'


    def writeOut(self, expected_json):
        with open(self.mockout, 'w+') as f:
            for x in expected_json:
                f.write("%s\n" % json.dumps(x, sort_keys=False))

    def readIn(self, file_name):
        return_list = []
        with open(file_name, 'r') as f:
            for line in f:
                return_list.append(json.loads(line))
        return return_list



    def test_parseAC(self):
        ac_line = 'AC   Q6NTF7; B0QYP0; B0QYP1;  B7TQM5; E9PF38; Q5JYL9; Q6IC87;'
        expected_json = OrderedDict([('_id', 'Q6NTF7'),
                                     ('ID',''),
                                     ('source', 'swiss'),
                                     ('PMID', []),
                                     ('sec_acc',
                                        ['B0QYP0','B0QYP1','B7TQM5','E9PF38','Q5JYL9','Q6IC87'])
                                    ])



        self.assertDictEqual(parseAC(ac_line,'swiss'), expected_json)

        ac_line = 'AC   Q6NTF7;'
        expected_json = OrderedDict([('_id', 'Q6NTF7'),
                                     ('ID',''),
                                     ('source','swiss'),
                                     ('PMID', []),
                                    ])

        self.assertDictEqual(parseAC(ac_line,'swiss'), expected_json)

    def test_Id(self):
        id_line = 'ID   003L_IIV3               Reviewed;         156 AA.'
        self.assertEqual('003L_IIV3', parseID(id_line))


    def test_pmidParser(self):
        mock_pmid = 'RX   PubMed=16571802; DOI=10.1128/JVI.80.8.3853-3862.2006;'
        expected_value = 16571802
        self.assertEqual(expected_value, parsePMID(mock_pmid))

    def test_parseENS(self):
        mock_line = 'DR   ENS; ENST00000348946; ENSP00000216123; ENSG00000100298. [Q6NTF7-2]'
        expected = OrderedDict([('iso',2), ('ENS', ['ENST00000348946','ENSP00000216123','ENSG00000100298'])])
        self.assertDictEqual(expected, parseENS(mock_line))

        mock_line = 'DR   ENS; ENST00000348946; ENSP00000216123; ENSG00000100298.'
        expected = OrderedDict([('iso',1), ('ENS', ['ENST00000348946','ENSP00000216123','ENSG00000100298'])])
        self.assertDictEqual(expected, parseENS(mock_line))

    def test_mainParser(self):
        self.maxDiff = None
        expected = [OrderedDict([
            ('_id', 'Q6NTF7'),
            ('ID', '003L_IIV3'),
            ('source', 'swiss'),
            ('PMID', [18945781,15461802,10591208,15489334,
                      12683974,16571802,16920826,18304004,
                      18779051,18299330,18827027,20308164,
                      20062055,21653666,21835787,22912627,
                      22457529,22915799,22001110,23097438]),
            ('sec_acc', ["B0QYP0", "B0QYP1", "B7TQM5",
                                     "E9PF38", "Q5JYL9", "Q6IC87",
                                     "QUEK123", "QUEK1234"]),
            ('gene', [OrderedDict([('iso', 1), ('ENS', ['ENST00000401756', 'ENSP00000385741','ENSG00000100298'])]),
                      OrderedDict([('iso', 2), ('ENS', ['ENST00000348946', 'ENSP00000216123','ENSG00000100298'])]),
                      OrderedDict([('iso', 3), ('ENS', ['ENST00000442487', 'ENSP00000411754','ENSG00000100298'])]),
                      OrderedDict([('iso', 4), ('ENS', ['ENST00000421988', 'ENSP00000393520','ENSG00000100298'])])
                    ])
            ])]

        self.writeOut(expected)

        with open('resources/actualOut.txt', 'w+') as f:
            mainParser(self.singleMock,'swiss', f)

        results = self.readIn('resources/actualOut.txt')
        expected = self.readIn(self.mockout)

        self.assertEqual(len(expected), len(results))
        self.assertEqual(expected, results)

    def test_MoreEntries(self):

        self.maxDiff = None
        expected = [OrderedDict([
            ('_id', 'Q6NTF7'),
            ('ID', '003L_IIV3'),
            ('source', 'swiss'),
            ('PMID', [18945781,15461802,10591208,15489334,
                      12683974,16571802,16920826,18304004,
                      18779051,18299330,18827027,20308164,
                      20062055,21653666,21835787,22912627,
                      22457529,22915799,22001110,23097438]),
            ('sec_acc', ["B0QYP0", "B0QYP1", "B7TQM5",
                                     "E9PF38", "Q5JYL9", "Q6IC87",
                                     "QUEK123", "QUEK1234"]),
            ('gene', [OrderedDict([('iso', 1), ('ENS', ['ENST00000401756', 'ENSP00000385741','ENSG00000100298'])]),
                      OrderedDict([('iso', 2), ('ENS', ['ENST00000348946', 'ENSP00000216123','ENSG00000100298'])]),
                      OrderedDict([('iso', 3), ('ENS', ['ENST00000442487', 'ENSP00000411754','ENSG00000100298'])]),
                      OrderedDict([('iso', 4), ('ENS', ['ENST00000421988', 'ENSP00000393520','ENSG00000100298'])])
                      ])
                    ]),

                    OrderedDict([
                        ('_id', 'Q1WBT4'),
                        ('ID', 'QUEK'),
                        ('source', 'swiss'),
                        ('PMID', [16571802]),
                    ])]


        self.writeOut(expected)
        with open('resources/actualOut.txt', 'w+') as f:
            mainParser(self.mockfile,'swiss', f)

        results = self.readIn('resources/actualOut.txt')
        expected = self.readIn(self.mockout)
        self.assertEqual(len(expected), len(results))
        self.assertItemsEqual(expected, results)





if __name__ == '__main__':
    unittest.main()
