import sys
import unittest
import us38
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/original.ged')
        # git_utils.abs_path('/testing/gedcom/us38_01.ged')
    ]
    txtfiles = ['us38_00.txt', 'us38_01.txt']
    results = []

    def test01(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[0]
        result = us38.compare(us38.list_upcoming_bdays(indivs, print_table=False), result_file)
        self.results += result
        self.assertTrue(len(result) == 0)

    def test02(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result_file = self.txtfiles[1]
        result = us38.compare(us38.list_upcoming_bdays(indivs, print_table=False, custom_date='2020-04-20'), result_file)
        self.results += result
        self.assertTrue(len(result) == 0)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
