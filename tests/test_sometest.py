import unittest

import mypackage


class SomethingTest1(unittest.TestCase):
    def test_is_running(self):
        s = mypackage.do_something()
        self.assertTrue(s == "Something")


class SomethingTest2(unittest.TestCase):
    def test_is_running(self):
        s = mypackage.do_something()
        self.assertFalse(s == "Otherthing")


if __name__ == '__main__':
    unittest.main()

# dummy test 1