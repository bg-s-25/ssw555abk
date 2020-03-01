import sys
import unittest
import us21
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):

    gedfiles = ['original.ged', 'us21_01.ged', 'us21_02.ged']
    results = []

    def test01(self): # correct roles
        indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[0])))[:2]
        result = us21.verify_correct_roles(indivs, fams)
        self.results += result
        self.assertEqual(len(result) == 0, True)

    def test02(self): # incorrect roles
        indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[1])))[:2]
        result = us21.verify_correct_roles(indivs, fams)
        self.results += result
        self.assertEqual(len(result) == 0, False)

    def test03(self): # incorrect roles
        indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[2])))[:2]
        result = us21.verify_correct_roles(indivs, fams)
        self.results += result
        self.assertEqual(len(result) == 0, False)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
