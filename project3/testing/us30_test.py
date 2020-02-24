import sys
import unittest
import us30
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):

    gedfiles = ['us30_01.ged']

    def test01(self): #married and divorced(dead)
        indivs, fams = gedcom.process_lines(gedcom.get_valid(gedcom.open_file(self.gedfiles[0])))
        self.assertEqual(us30.listmarried(indivs, fams)[0], True)


def tester():
    unittest.main()

if __name__ == '__main__':
    # Run tests
    unittest.main()
