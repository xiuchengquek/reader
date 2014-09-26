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

        Reader(self.mock_file, 20)
        expect_output = 'outdir/file_0'
        with open(self.mock_expected) as f:
            mock_expected = f.read()

        mock_expected = mock_expected.split('\n')

        with open(expect_output) as f:
            actual_output = f.read()
        actual_output = actual_output.split('\n')

        self.assertItemsEqual(mock_expected, actual_output)


    def testExpectedB(self):
        self.maxDiff = None
        expected_files = ['outdir/file_0', 'outdir/file_1', 'outdir/file_2']
        Reader(self.mock_file, 5)
        expected_mock_files = ['mockfiles/expected_B_0.txt', 'mockfiles/expected_B_1.txt', 'mockfiles/expected_B_2.txt']
        expected_contents = []
        actual_contents = []

        for i in expected_files:
            with open(i, 'r') as f:
                actual_contents.append(f.read())
        for i in expected_mock_files:
            with open(i, 'r') as f:
                expected_contents.append(f.read())

        content = ["outdir/%s" % x for x in os.listdir('outdir') if not x.startswith('.')]
        self.assertItemsEqual(expected_files, content)
        self.assertItemsEqual(expected_contents, actual_contents)


    def tearDown(self):
        content = ["outdir/%s" % x for x in os.listdir('outdir') if not x.startswith('.')]
        [os.unlink(x) for x in content]


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataFinder)
unittest.TextTestRunner(verbosity=2).run(suite)






