import sys
import unittest
import us39
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import compare
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/original.ged'),
        git_utils.abs_path('/testing/gedcom/us39_01.ged')
    ]
    txtfiles = [
        git_utils.abs_path('/testing/sprint2/us39_01.txt'), 
        git_utils.abs_path('/testing/sprint2/us39_02.txt'), 
        git_utils.abs_path('/testing/sprint2/us39_03.txt')
    ]
    results = []

    def test01(self):
        fams = main_parser.tester(self.gedfiles[0])[1]
        result_file = self.txtfiles[0]
        result = compare.compare(us39.list_upcoming_annivs(fams, print_table=False, custom_date='2020-04-20'), result_file, "US39")
        self.results += result
        self.assertTrue(len(result) == 0)

    def test02(self):
        fams = main_parser.tester(self.gedfiles[0])[1]
        result_file = self.txtfiles[1]
        result = compare.compare(us39.list_upcoming_annivs(fams, print_table=False, custom_date='2020-02-14'), result_file, "US39")
        self.results += result
        self.assertTrue(len(result) == 0)

    def test03(self):
        fams = main_parser.tester(self.gedfiles[1])[1]
        result_file = self.txtfiles[2]
        result = compare.compare(us39.list_upcoming_annivs(fams, print_table=False, custom_date='2020-12-30'), result_file, "US39")
        self.results += result
        self.assertTrue(len(result) == 0)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
