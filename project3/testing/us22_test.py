import sys
import unittest
import us22
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):

    gedfiles = ['original.ged', 'us22_01.ged', 'us22_02.ged']
    results = []

    def test01(self): # ged contains no repeated ids
        indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[0])))[2:]
        result = us22.verify_unique_ids(indivs, fams)
        self.results += [result]
        self.assertEqual(result[0], True)

    def test02(self): # ged contains repeated individual id
        indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[1])))[2:]
        result = us22.verify_unique_ids(indivs, fams)
        self.results += [result]
        self.assertEqual(result[0], False)

    def test03(self): # ged contains repeated individual id
        indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[2])))[2:]
        result = us22.verify_unique_ids(indivs, fams)
        self.results += [result]
        self.assertEqual(result[0], False)

def test_results():
    return Tests.results

if __name__ == '__main__':
    # Run tests
    unittest.main()
