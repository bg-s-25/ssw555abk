import sys
import unittest
import us23
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us23_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us23_02.ged'),
        git_utils.abs_path('/testing/gedcom/original.ged'),
    ]
    results = []

    def test01(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        result = us23.verify_unique_namesbdate(indivs)
        self.results += result
        self.assertEqual(len(result) == 0, False)
   
    def test02(self):
        indivs = main_parser.tester(self.gedfiles[1])[0]
        result = us23.verify_unique_namesbdate(indivs)
        self.results += result
        self.assertEqual(len(result) == 0, False)

    def test03(self):
        indivs = main_parser.tester(self.gedfiles[2])[0]
        result = us23.verify_unique_namesbdate(indivs)
        self.results += result
        self.assertEqual(len(result) == 0, True)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
