import sys
import unittest
import us27
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import compare
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us27_01.ged')
    ]
    txtfiles = ['us27_01.txt', 'us27_02.txt']
    results = []

    def test01(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[0]
        result = compare.compare(us27.indiv_prettytable(indivs), result_file, "US27")
        self.results += result
        self.assertEqual(len(result) == 0, True)
    
    def test02(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[1]
        result = compare.compare(us27.indiv_prettytable(indivs), result_file, "US27")
        self.results += result
        self.assertEqual(len(result) == 0, False)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
