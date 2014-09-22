__author__ = 'quek'


import unittest
import os
from itertools import repeat






from reader import Reader






class TestDataFinder(unittest.TestCase):

    def setUp(self):
        self.mock_file ='mockInput.txt'
        self.out_dir = os.path.join(os.getcwd(), 'outdir')


    def testBasicInput(self):
        mock_data = []
        for x in range(1,11):
            for y in range(1,11):
                mock_data.append('%i\t%i' % (x,x))
        mock_length = len(mock_data)
        mock_data = "\n".join(mock_data)

        with open(self.mock_file, 'w+') as f:
            f.write(mock_data)
        f.close()
        self.assertEqual(mock_length,  sum(1 for line in open(self.mock_file)))
        Reader(self.mock_file, 10)
        content = ["outdir/%s" % x for x in os.listdir('outdir') if not x.startswith('.')]
        self.assertEqual(len(content), 10)
        for x in content:
            self.assertEqual(sum(1 for line in open(x)),10)



    def testMorethanLineBreak(self):
        mock_data = []
        for x in range(1,11):
            for y in range(1,21):
                mock_data.append('%i\t%i' % (x,x))
        mock_length = len(mock_data)
        mock_data = "\n".join(mock_data)
        with open(self.mock_file, 'w+') as f:
            f.write(mock_data)
            f.close()
            self.assertEqual(mock_length,  sum(1 for line in open(self.mock_file)))
            Reader(self.mock_file, 10)
            content = ["outdir/%s" % x for x in os.listdir('outdir') if not x.startswith('.')]
            self.assertEqual(len(content), 10)
            for x in content:
                self.assertEqual(sum(1 for line in open(x)),20)

    def testFileNames(self):
        expected_files = ['file_%i' % x for x in range(10)]
        mock_data = []
        for x in range(1,11):
            for y in range(1,11):
                mock_data.append('%i\t%i' % (x,x))
        mock_length = len(mock_data)
        mock_data = "\n".join(mock_data)

        with open(self.mock_file, 'w+') as f:
            f.write(mock_data)
        f.close()
        Reader(self.mock_file, 10)
        content = [x for x in os.listdir('outdir') if not x.startswith('.')]
        self.assertItemsEqual(sorted(expected_files), sorted(content))

    def testOddList(self):
        expected_files = ['1_10_1','11_20_2','21_30_3']
        mock_data = []
        for x in range(1,30):
            mock_data.append('%i\t%i' % (x,x))
        mock_length = len(mock_data)
        mock_data = "\n".join(mock_data)

        with open(self.mock_file, 'w+') as f:
            f.write(mock_data)
        f.close()
        Reader(self.mock_file, 10)
        content = ["outdir/%s" % x for x in os.listdir('outdir') if not x.startswith('.')]
        self.assertEqual(len(content), 3)


    def testOddName(self):
        expected_files = ['file_0','file_1','file_2']
        mock_data = []
        for x in range(1,31):
            mock_data.append('%i\t%i' % (x,x))
        mock_length = len(mock_data)
        mock_data = "\n".join(mock_data)

        with open(self.mock_file, 'w+') as f:
            f.write(mock_data)
        f.close()
        Reader(self.mock_file, 10)
        content = [x for x in os.listdir('outdir') if not x.startswith('.')]
        self.assertItemsEqual(sorted(expected_files), sorted(content))



    def testFinal(self):
        mock_data = list(repeat(6,5))
        mock_data.extend(repeat(7,5))
        mock_data.extend(repeat(8,6))
        mock_data.extend(repeat(10,2))
        mock_data.extend(repeat(12,14))
        mock_data = [str(x) for x in mock_data]
        mock_length = len(mock_data)

        with open(self.mock_file, 'w+') as f:
            for x in mock_data:
                f.write('%s\t%s\n' % (x,x))
        f.close()

        Reader(self.mock_file, 10)
        content = [x for x in os.listdir('outdir') if not x.startswith('.')]
        self.assertEqual(len(content), 2)






    def tearDown(self):
        content = ["outdir/%s" % x for x in os.listdir('outdir') if not x.startswith('.')]
        os.unlink(self.mock_file)
        [os.unlink(x) for x in content]


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataFinder)
unittest.TextTestRunner(verbosity=2).run(suite)






