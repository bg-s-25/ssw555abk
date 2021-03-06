import sys
import unittest
import us03
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/original.ged'), 
        git_utils.abs_path('/testing/gedcom/us03_02.ged')
    ]
    results = []

    def test01(self):
        individuals = main_parser.tester(self.gedfiles[0])[0]
        result = us03.bbd(individuals)
        self.results += result
        self.assertEqual(len(result) == 0, True)

    def test02(self):
        individuals = main_parser.tester(self.gedfiles[1])[0]
        result = us03.bbd(individuals)
        self.results += result
        self.assertEqual(len(result) == 0, False)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()