import sys
import unittest
import us06
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us06_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us06_02.ged')
    ]
    results = []

    def test01(self): 
        indivs, fams = main_parser.tester(self.gedfiles[0])[:2]
        result = us06.divorce_before_death(indivs, fams)
        self.results += result
        self.assertEqual(len(result) == 0, False)
   
    def test02(self):
        indivs, fams = main_parser.tester(self.gedfiles[1])[:2]
        result = us06.divorce_before_death(indivs, fams)
        self.results += result
        self.assertEqual(len(result) == 0, True)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
