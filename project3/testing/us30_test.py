import sys
import unittest
import us30
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):
    
    gedfiles = ['us30_01.ged','us30_02.ged','us30_03.ged']

    def test01(self): #married
        indivs, fams = gedcom.tester(self.gedfiles[0])[:2]
        self.assertEqual(us30.listmarried(indivs, fams), True)

    def test02(self): #married and divorced(not dead)
        indivs, fams = gedcom.tester(self.gedfiles[1])[:2]
        self.assertEqual(us30.listmarried(indivs, fams), True)

    def test03(self): #married and divorced(not dead)
        indivs, fams = gedcom.tester(self.gedfiles[2])[:2]
        self.assertEqual(us30.listmarried(indivs, fams), True)

def tester():
    unittest.main()

if __name__ == '__main__':
    # Run tests
    unittest.main()
