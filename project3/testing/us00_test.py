# This is a dummy file for the tester

import unittest
import us00

class Tests(unittest.TestCase):

    def test01(self):
        self.assertEqual(us00.do_something(), 'something')

if __name__ == '__main__':
    # Run tests
    unittest.main()
