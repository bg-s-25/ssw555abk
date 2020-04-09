import sys
import unittest
import us29
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import compare
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us29_01.ged')
    ]
    txtfiles = [
        git_utils.abs_path('/testing/sprint1/us29_01.txt'), 
        git_utils.abs_path('/testing/sprint1/us29_02.txt')
    ]
    results = []

    def test01(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[0]
        result = compare.compare(us29.listdeceased(indivs, print_table=False), result_file, "US29")
        self.results += result
        self.assertEqual(len(result) == 0, True)

    def test02(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[1]
        result = compare.compare(us29.listdeceased(indivs, print_table=False), result_file, "US29")
        self.results += result
        self.assertEqual(len(result) == 0, False)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
