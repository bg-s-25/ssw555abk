import sys
import unittest
import us21
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):

    ged_file_01 = 'us21.ged'
    indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(ged_file_01)))

    def test01(self):
        self.assertEqual(us21.verify_correct_roles(self.indivs, self.fams)[0], False)

if __name__ == '__main__':
    # Run tests
    unittest.main()
