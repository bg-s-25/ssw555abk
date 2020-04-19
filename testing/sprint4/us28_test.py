import sys
import unittest
import us28
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import compare
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us28_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us28_02.ged'),
        git_utils.abs_path('/testing/gedcom/original.ged')
    ]
    txtfiles = [
        git_utils.abs_path('/testing/sprint4/us28_01.txt'),
        git_utils.abs_path('/testing/sprint4/us28_02.txt'),
        git_utils.abs_path('/testing/sprint4/us28_original.txt')
    ]
    results = []

    def test01(self): 
        indivs, families = main_parser.tester(self.gedfiles[0])[:2]
        result_file = self.txtfiles[0]
        result = compare.compare(us28.list_siblings(indivs, families, print_table=False), result_file, 'US28')
        self.results += result
        self.assertEqual(len(result) == 0, True)

    def test02(self): 
        indivs, families = main_parser.tester(self.gedfiles[1])[:2]
        result_file = self.txtfiles[1]
        result = compare.compare(us28.list_siblings(indivs, families, print_table=False), result_file, 'US28')
        self.results += result
        self.assertEqual(len(result) == 0, True)

    def test03(self): 
        indivs, families = main_parser.tester(self.gedfiles[2])[:2]
        result_file = self.txtfiles[2]
        result = compare.compare(us28.list_siblings(indivs, families, print_table=False), result_file, 'US28')
        self.results += result
        self.assertEqual(len(result) == 0, True)
    

def test_results():
    return Tests.results

if __name__=='__main__':
    unittest.main()