import sys
import unittest
import us33
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import compare
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us33_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us33_02.ged')
    ]
    txtfiles = [
        git_utils.abs_path('/testing/sprint2/us33_01.txt')
    ]
    results = []

    def test01(self): 
        indivs, fams = main_parser.tester(self.gedfiles[0])[:2]
        result_file = self.txtfiles[0]
        result = compare.compare(us33.listorphaned(indivs, fams), result_file, 'US33')
        self.results += result
        self.assertEqual(len(result) == 0, True)
        
    '''
    def test02(self): 
        indivs, fams = main_parser.tester(self.gedfiles[1])[:2]
'''
def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
