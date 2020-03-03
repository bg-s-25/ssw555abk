import sys
import unittest
import us29
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
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
        test_file = us29.listdeceased(indivs)
        result_file = self.txtfiles[0]
        result = us29.compare(test_file, result_file)
        self.results += result
        self.assertEqual(len(result) == 0, True)

    def test02(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        test_file = us29.listdeceased(indivs)
        result_file = self.txtfiles[1]
        result = us29.compare(test_file, result_file)
        self.results += result
        self.assertEqual(len(result) == 0, False)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
