import sys
import unittest
import us22
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):

    gedfiles = ['original.ged', 'us22_01.ged', 'us22_02.ged']

    def test01(self): # ged contains no repeated ids
        indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[0])))[2:]
        self.assertEqual(us22.verify_unique_ids(indivs, fams)[0], True)

    def test02(self): # ged contains repeated individual id
        indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[1])))[2:]
        self.assertEqual(us22.verify_unique_ids(indivs, fams)[0], False)

    def test03(self): # ged contains repeated individual id
        indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[2])))[2:]
        self.assertEqual(us22.verify_unique_ids(indivs, fams)[0], False)

def tester():
    unittest.main()

if __name__ == '__main__':
    # Run tests
    unittest.main()
