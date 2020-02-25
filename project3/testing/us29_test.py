import sys
import unittest
import us29
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):

    gedfiles = ['us29_01.ged']

    def test01(self): 
        indivs = gedcom.tester(self.gedfiles[0])[0]
        test_file = open(us29.listdeceased(indivs), "r")
        result_file = open("us29_01.txt", "r")
        self.assertEqual(test_file.read(), result_file.read())
        test_file.close()
        result_file.close()

def tester():
    unittest.main()

if __name__ == '__main__':
    # Run tests
    unittest.main()
