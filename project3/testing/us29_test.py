import sys
import unittest
import us29
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):

    gedfiles = ['us29_01.ged']

    def test01(self): # correct roles
        #isn't it check_valid
        #can't just call collections[0] ??
        indivs = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[0])))
        self.assertEqual(us29.listdeceased(indivs)[0], True)
        
        #indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[0])))
        #self.assertEqual(us30.listmarried(indivs, fams)[0], True)


def tester():
    unittest.main()

if __name__ == '__main__':
    # Run tests
    unittest.main()
