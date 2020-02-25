import sys
import unittest
import us03
sys.path.insert(0, '../')
import gedcom


class Tests(unittest.TestCase):

    gedfiles = ['original.ged']

    def test01(self):
        individuals, families, indiv_ids, fam_ids = gedcom.tester(self.gedfiles[0])
        self.assertEqual(us03.bbd(individuals, families, indiv_ids, fam_ids), True)

def tester():
    unittest.main()

if __name__ == '__main__':
    # Run tests
    unittest.main()