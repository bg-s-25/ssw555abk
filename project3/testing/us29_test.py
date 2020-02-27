import sys
import unittest
import us29
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):
    gedfiles = ['us29_01.ged']
    txtfiles = ['us29_01.txt', 'us29_01.1.txt']

    def test01(self): 
        indivs = gedcom.tester(self.gedfiles[0])[0]
        test_file = us29.listdeceased(indivs)
        result_file = self.txtfiles[0]
        self.assertEqual(us29.compare(test_file, result_file)[0], True)

    def test02(self): 
        indivs = gedcom.tester(self.gedfiles[0])[0]
        test_file = us29.listdeceased(indivs)
        result_file = self.txtfiles[1]
        self.assertEqual(us29.compare(test_file, result_file)[0], False)

def tester():
    unittest.main()

if __name__ == '__main__':
    # Run tests
    unittest.main()