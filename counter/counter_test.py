__author__ = 'quek'
__author__ = 'quek'

import unittest
import os
import json
from collections import OrderedDict

from counter.counter import Printer


class TestPrinter(unittest.TestCase):
    def testPrinter(self):
        expected_array = []
        expected_array.append(
            json.dumps(OrderedDict([('PMID', '1'), ('type', 'classA'), ('term', 'termA'), ('count', '20')])))
        expected_array.append(
            json.dumps(OrderedDict([('PMID', '1'), ('type', 'classB'), ('term', 'termB'), ('count', '10')])))

        mock_counter = OrderedDict([('termA', '20'), ('termB', '10')])
        mock_dict = OrderedDict([('termA', 'classA'), ('termB', 'classB')])
        return_line = []

        Printer('outdir/mock_printer.txt', '1', mock_counter, mock_dict)
        with open('outdir/mock_printer.txt') as f:
            for line in f:
                return_line.append(line.strip())

        return_line = ",".join(return_line)
        expected_line = ",".join(expected_array)
        self.assertEqual(expected_line, return_line)


    def tearDown(self):
        os.unlink('outdir/mock_printer.txt')


class TestDataFinder(unittest.TestCase):
    pass

    """

   def setUp(self):
       self.mock_file ='mockInput.txt'
       self.out_dir = os.path.join(os.getcwd(), 'outdir')

   def repeat_maker(self, id, org, term, repeats):
       line = "%s\t%s\t%s\n" % (id, org, term)
       return repeat(line, repeats)


   def interpret_results(self, in_file):
       return_array = []
       with in_file as f:
           for line in f:
               fields = line.split('\t')
               return_array.append(tuple(fields))

       return return_array



   def tearDown(self):
       content = ["outdir/%s" % x for x in os.listdir('outdir') if not x.startswith('.')]
       os.unlink(self.mock_file)
       [os.unlink(x) for x in content]



   def testExpectedReturn(self):
       expected_value = [('1','orgA','termA',19),('1','orgA','termB',14),
                         ('2', 'orgB','termA,',4),('2','orgB', 'termC',3)]
       mock_fh = open(self.mock_file, 'w+')
       for x in expected_value:
           lines = self.repeat_maker(x[0],x[1],x[2],x[3])
           mock_fh.write(lines)

       mock_fh.close()
   """


suite = unittest.TestLoader().loadTestsFromTestCase(TestPrinter)
unittest.TextTestRunner(verbosity=2).run(suite)






