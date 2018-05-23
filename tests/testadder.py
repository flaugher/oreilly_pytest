import unittest
from proj.adder import adder

# run: PYTHONPATH=. pytest tests/*.py

class TestAdder(unittest.TestCase):
    def test_simple(self):
        res = adder(2, 3)
        self.assertEquals(res, 5)

# pytest-style test.  Notice no class.  More Pythonic.  Less boilerplate.
def test_add():
    res = adder(2, 3)
    assert res == 5
