import sys
import unittest
import us30
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):
    
    gedfiles = ['us30_01.ged','us30_02.ged','us30_03.ged']

    def test01(self): #married and dead(single??)
        fams = gedcom.tester(self.gedfiles[0])[1]
        self.assertEqual(us30.listmarried(fams), True)

    def test02(self): #married and divorced(not dead)
        fams = gedcom.tester(self.gedfiles[1])[1]
        self.assertEqual(us30.listmarried(fams), True)

    def test03(self): #married and divorced(not dead)
        fams = gedcom.tester(self.gedfiles[1])[2]          #this is throwing errors!! us30_03
        self.assertEqual(us30.listmarried(fams), True)

def tester():
    unittest.main()

if __name__ == '__main__':
    # Run tests
    unittest.main()
