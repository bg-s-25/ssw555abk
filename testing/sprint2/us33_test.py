import sys
import unittest
import us33
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us33_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us33_02.ged')
    ]
    txtfiles = ['us33_01.txt']
    results = []

    def test01(self): 
        indivs, fams = main_parser.tester(self.gedfiles[0])[:2]
        test_file = us33.listorphaned(indivs, fams)
        result_file = self.txtfiles[0]
        result = us33.compare(test_file, result_file)
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
