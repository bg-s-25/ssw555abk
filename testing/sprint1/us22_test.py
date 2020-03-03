import sys
import unittest
import us22
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import main_parser

class Tests(unittest.TestCase):

    gedfiles = [
        git_utils.abs_path('/testing/gedcom/original.ged'), 
        git_utils.abs_path('/testing/gedcom/us22_01.ged'),
        git_utils.abs_path('/testing/gedcom/us22_02.ged'),
    ]
    results = []

    def test01(self): # ged contains no repeated ids
        indivs, fams = main_parser.process_lines(main_parser.get_valid(main_parser.open_file(self.gedfiles[0])))[2:]
        result = us22.verify_unique_ids(indivs, fams)
        self.results += result
        self.assertEqual(len(result) == 0, True)

    def test02(self): # ged contains repeated individual id
        indivs, fams = main_parser.process_lines(main_parser.get_valid(main_parser.open_file(self.gedfiles[1])))[2:]
        result = us22.verify_unique_ids(indivs, fams)
        self.results += result
        self.assertEqual(len(result) == 0, False)

    def test03(self): # ged contains repeated individual id
        indivs, fams = main_parser.process_lines(main_parser.get_valid(main_parser.open_file(self.gedfiles[2])))[2:]
        result = us22.verify_unique_ids(indivs, fams)
        self.results += result
        self.assertEqual(len(result) == 0, False)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
