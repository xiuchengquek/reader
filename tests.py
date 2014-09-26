__author__ = 'quek'

import unittest
import os

from reader import Reader


class TestDataFinder(unittest.TestCase):
    def setUp(self):
        self.mock_file = 'mockfiles/example_A.txt'
        self.mock_expected = 'mockfiles/expected_A.txt'
        self.out_dir = os.path.join(os.getcwd(), 'outdir')


    def testExampleA(self):
        self.maxDiff = None

        Reader(self.mock_file)
        expect_output = 'outdir/file_0'
        with open(self.mock_expected) as f:
            mock_expected = f.read()

        mock_expected = mock_expected.split('\n')

        with open(expect_output) as f:
            actual_output = f.read()
        actual_output = actual_output.split('\n')

        self.assertItemsEqual(mock_expected, actual_output)


    def tearDown(self):
        content = ["outdir/%s" % x for x in os.listdir('outdir') if not x.startswith('.')]
        [os.unlink(x) for x in content]


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataFinder)
unittest.TextTestRunner(verbosity=2).run(suite)






