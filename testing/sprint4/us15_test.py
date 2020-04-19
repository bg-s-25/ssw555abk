import sys
import unittest
import us15
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import compare
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us15_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us15_02.ged')
    ]

    errors = []

    def test01(self):
        families = main_parser.tester(self.gedfiles[0])[1]
        error = us15.number_siblings(families)
        self.errors += error
        self.assertEqual(len(error) == 0, True)
    
    def test02(self):
        families = main_parser.tester(self.gedfiles[1])[1]
        error = us15.number_siblings(families)
        self.errors += error
        self.assertEqual(len(error) == 0, False)


def test_errors():
    return Tests.errors

if __name__ == '__main__':
    # Run tests
    unittest.main()