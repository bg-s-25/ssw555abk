import sys
import unittest
import us30
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):
    gedfiles = ['us30_01.ged','us30_02.ged']
    txtfiles = ['us30_01.txt','us30_02.txt']

    def test01(self): 
        indivs, fams = gedcom.tester(self.gedfiles[0])[:2]
        test_file = us30.listmarried(indivs, fams)
        result_file = self.txtfiles[0]
        self.assertEqual(us30.compare(test_file, result_file)[0], True)
    
    def test02(self): 
        indivs, fams = gedcom.tester(self.gedfiles[1])[:2]
        test_file = us30.listmarried(indivs, fams)
        result_file = self.txtfiles[1]
        self.assertEqual(us30.compare(test_file, result_file)[0], False)

def tester():
    unittest.main()

if __name__ == '__main__':
    # Run tests
    unittest.main()