import sys
import unittest
import us17
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import compare
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us17_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us17_02.ged'),
        git_utils.abs_path('/testing/gedcom/original.ged')
    ]
    errors = []

    def test01(self):
        indivs, fams = main_parser.tester(self.gedfiles[0])[:2]
        res = us17.check_marr_child(indivs, fams)
        self.errors += res
        self.assertEqual(len(res), 1)

    def test02(self):
        indivs, fams = main_parser.tester(self.gedfiles[1])[:2]
        res = us17.check_marr_child(indivs, fams)
        self.errors += res
        self.assertEqual(len(res), 2)

    def test03(self):
        indivs, fams = main_parser.tester(self.gedfiles[2])[:2]
        res = us17.check_marr_child(indivs, fams)
        self.errors += res
        self.assertEqual(len(res), 0)

def test_errors():
    return Tests.errors

if __name__ == '__main__':
    # Run tests
    unittest.main()
