# import os
# import sys
# import logging
import unittest
import numpy as np

# import ssl
# import matlab.engine
# #matlab_engine = matlab.engine.start_matlab()
# path_to_matlab_code="./ACA"

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


# class SomethingTestWithMatlab(unittest.TestCase):
#     logger = logging.getLogger(__name__)
#     logging.basicConfig(level=logging.INFO)
#
#     def __init__(self, *args, **kwargs):
#         super(SomethingTestWithMatlab, self).__init__(*args, **kwargs)
#         self.matlab_engine = None
#         path_valid = os.path.exists(path_to_matlab_code)
#         init_engine = True
#
#         if 'matlab.engine' not in sys.modules:
#             self.logger.warning("matlab package not found")
#             init_engine = False
#         if not path_valid:
#             self.logger.warning("Invalid path to Matlab code")
#             init_engine = False
#
#         if init_engine:
#             self.matlab_engine = matlab.engine.start_matlab()
#             self.matlab_engine.cd(path_to_matlab_code)
#
#     def __del__(self):
#         if self.matlab_engine is not None:
#             self.matlab_engine.quit()
#
#     def test_all_features(self):
#
#         if self.matlab_engine is None:
#             self.skipTest("Matlab engine not available")



if __name__ == '__main__':
    unittest.main()

# dummy test 1
# dummy text 2
# dummy test 3