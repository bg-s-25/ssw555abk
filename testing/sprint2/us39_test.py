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
        git_utils.abs_path('/testing/gedcom/original.ged')
        # git_utils.abs_path('/testing/gedcom/us39_01.ged')
    ]
    txtfiles = ['us39_00.txt', 'us39_01.txt']
    results = []

    def test01(self):
        fams = main_parser.tester(self.gedfiles[0])[1]
        result_file = self.txtfiles[0]
        result = compare.compare(us39.list_upcoming_annivs(fams, print_table=True), result_file, "US39")
        self.results += result
        self.assertTrue(len(result) == 0)

    def test02(self):
        fams = main_parser.tester(self.gedfiles[0])[1]
        result_file = self.txtfiles[1]
        result = compare.compare(us39.list_upcoming_annivs(fams, print_table=True, custom_date='2020-04-20'), result_file, "US39")
        self.results += result
        self.assertTrue(len(result) == 0)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
