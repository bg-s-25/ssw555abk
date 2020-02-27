import sys
import unittest
import us02
sys.path.insert(0, '../')
import gedcom

class Tests(unittest.TestCase):

    gedfiles = ['original.ged']

    def test01(self):
        individuals, families = gedcom.tester(self.gedfiles[0])[:2]
        print(us02.bbm(individuals,families))
        self.assertEqual(us02.bbm(individuals, families)[0], True)


def tester():
    unittest.main()

if __name__ == '__main__':
    # Run tests
    unittest.main()