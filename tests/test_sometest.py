import unittest
import numpy as np
import matlab.engine
#matlab_engine = matlab.engine.start_matlab()

import mypackage


class SomethingTest1(unittest.TestCase):
    def test_is_running(self):
        s = mypackage.do_something()
        self.assertTrue(s == "Something")


class SomethingTest2(unittest.TestCase):
    def test_is_running(self):
        s = mypackage.do_something()
        self.assertFalse(s == "Otherthing")


class SomethingTest3(unittest.TestCase):
    def test_is_running(self):
        s = np.floor(3.5).astype(int)
        self.assertTrue(s == 3)


if __name__ == '__main__':
    unittest.main()

# dummy test 1
# dummy text 2
# dummy test 3