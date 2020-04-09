import sys
import unittest
import us35
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import compare
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us35_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us35_02.ged')
    ]
    txtfiles = [
        git_utils.abs_path('/testing/sprint3/us35_01.txt')
    ]
    results = []

    def test01(self): 
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[0]
        result = compare.compare(us35.list_recently_born(indivs, print_table=False), result_file, 'US35')
        self.results += result
        self.assertEqual(len(result) == 0, True)
    
    def test02(self): 
        indivs = main_parser.tester(self.gedfiles[1])[0]
        result_file = self.txtfiles[0]
        result = compare.compare(us35.list_recently_born(indivs, print_table=False), result_file, 'US35')
        self.results += result
        self.assertEqual(len(result) == 0, False)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
