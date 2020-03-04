import sys
import unittest
import us31
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us31_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us31_02.ged')
    ]
    txtfiles = ['us31_01.txt','us31_02.txt']
    results = []

    def test01(self): 
        indivs = main_parser.tester(self.gedfiles[0])[0]
        test_file = us31.listsingle(indivs)
        result_file = self.txtfiles[0]
        result = us31.compare(test_file, result_file)
        self.results += result
        self.assertEqual(len(result) == 0, True)
      
    def test02(self):
        indivs = main_parser.tester(self.gedfiles[1])[0]
        test_file = us31.listsingle(indivs)
        result_file = self.txtfiles[1]
        result = us31.compare(test_file, result_file)
        self.results += result
        self.assertEqual(len(result) == 0, False)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
