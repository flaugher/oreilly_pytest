import unittest
from proj.adder import adder

class TestAdder(unittest.TestCase):
    def test_simple(self):
        res = adder(2, 3)
        self.assertEquals(res, 5)
