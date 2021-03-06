import sys
import unittest
import us04
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import compare
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us04_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us04_02.ged'),
        git_utils.abs_path('/testing/gedcom/original.ged')
    ]

    errors = []

    def test01(self):
        families = main_parser.tester(self.gedfiles[0])[1]
        error = us04.marriage_before_divorce(families)
        self.errors += error
        self.assertEqual(len(error) == 0, False)

    def test02(self):
        families = main_parser.tester(self.gedfiles[1])[1]
        error = us04.marriage_before_divorce(families)
        self.errors += error
        self.assertEqual(len(error) == 0, False)

    def test03(self):
        families = main_parser.tester(self.gedfiles[2])[1]
        error = us04.marriage_before_divorce(families)
        self.errors += error
        self.assertEqual(len(error) == 0, True)

def test_errors():
    return Tests.errors

if __name__ == '__main__':
    # Run tests
    unittest.main()