from unittest import TestCase

from mypackage import something


class SomethingTest1(TestCase):
    def test_is_running(self):
        s = something.do_something()
        self.assertTrue(s == "Something")


class SomethingTest2(TestCase):
    def test_is_running(self):
        s = something.do_something()
        self.assertTrue(s == "Otherthing")
