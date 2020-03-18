import sys
import unittest
import us38
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import compare
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/original.ged')
    ]
    txtfiles = ['us38_00.txt', 'us38_01.txt', 'us38_03.txt']
    results = []

    def test01(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[0]
        result = compare.compare(us38.list_upcoming_bdays(indivs, print_table=False, custom_date='2020-04-20'), result_file, "US38")
        self.results += result
        self.assertTrue(len(result) == 0)

    def test02(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[1]
        result = compare.compare(us38.list_upcoming_bdays(indivs, print_table=False, custom_date='2020-06-01'), result_file, "US38")
        self.results += result
        self.assertTrue(len(result) == 0)

    def test03(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[2]
        result = compare.compare(us38.list_upcoming_bdays(indivs, print_table=False, custom_date='2020-12-31'), result_file, "US38")
        self.results += result
        self.assertTrue(len(result) == 0)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
