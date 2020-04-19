import sys
import unittest
import us01
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import compare
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/griffinfamilytest.ged'), 
        git_utils.abs_path('/testing/gedcom/us01_01.ged'),
        git_utils.abs_path('/testing/gedcom/us01_02.ged'),
        git_utils.abs_path('/testing/gedcom/us01_03.ged'),
        git_utils.abs_path('/testing/gedcom/us01_04.ged'),
    ]

    errors = []

    def test01(self): #birthdays 
        individuals, families = main_parser.tester(self.gedfiles[1])[:2]
        error = us01.check_all_dates(individuals, families)
        self.errors += error
        self.assertEqual(len(error) == 0, False)

    def test02(self): #death date
        individuals, families = main_parser.tester(self.gedfiles[2])[:2]
        error = us01.check_all_dates(individuals, families)
        self.errors += error
        self.assertEqual(len(error) == 0, False)

    def test03(self): #married date
        individuals, families = main_parser.tester(self.gedfiles[3])[:2]
        error = us01.check_all_dates(individuals, families)
        self.errors += error
        self.assertEqual(len(error) == 0, False)

    def test04(self): #divorced date
        individuals, families = main_parser.tester(self.gedfiles[4])[:2]
        error = us01.check_all_dates(individuals, families)
        self.errors += error
        self.assertEqual(len(error) == 0, False)
    
    def test05(self): #normal
        individuals, families = main_parser.tester(self.gedfiles[0])[:2]
        error = us01.check_all_dates(individuals, families)
        self.errors += error
        self.assertEqual(len(error) == 0, True)

def test_errors():
    return Tests.errors

if __name__ == '__main__':
    # Run tests
    unittest.main()