# This is a dummy file for the teser

import unittest
import US00

class Tests(unittest.TestCase):

    def test01(self):
        self.assertEqual(US00.do_something(), 'something')

if __name__ == '__main__':
    # Run tests
    unittest.main()
