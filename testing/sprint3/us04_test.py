import sys
import unittest
import us36
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
import git_utils
import compare
import main_parser

class Tests(unittest.TestCase):
    def test01(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        self.assertEqual()

    def test02(self):
        indivs = main_parser.tester(self.gedfiles[0])[0]
        self.assertEqual()

if __name__ == '__main__':
    # Run tests
    unittest.main()