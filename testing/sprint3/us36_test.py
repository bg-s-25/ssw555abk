import sys
import unittest
import us36
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import compare
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us36_01.ged')
    ]
    txtfiles = [
        git_utils.abs_path('/testing/sprint3/us36_01.txt')
    ]
    results = []

    def test01(self): 
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[0]
        result = compare.compare(us36.list_recently_deceased(indivs, print_table=False, custom_date='2020-04-01'), result_file, 'US36')
        self.results += result
        self.assertEqual(len(result) == 0, True)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
