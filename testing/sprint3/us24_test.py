import sys
import unittest
import us24
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/us24_01.ged'), 
        git_utils.abs_path('/testing/gedcom/us24_02.ged'),
        git_utils.abs_path('/testing/gedcom/original.ged')
    ]
    results = []

    def test01(self):
        fams = main_parser.tester(self.gedfiles[0])[1]
        result = us24.verify_unique_families(fams)
        self.results += result
        self.assertEqual(len(result) == 0, False)
   
    def test02(self):
        fams = main_parser.tester(self.gedfiles[1])[1]
        result = us24.verify_unique_families(fams)
        self.results += result
        self.assertEqual(len(result) == 0, False)

    def test03(self):
        fams = main_parser.tester(self.gedfiles[2])[1]
        result = us24.verify_unique_families(fams)
        self.results += result
        self.assertEqual(len(result) == 0, True)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
