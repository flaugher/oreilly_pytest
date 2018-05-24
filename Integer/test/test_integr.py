#!/usr/bin/env python
from pdb import set_trace as debug
from integr import parse

def test_basic():
    istring = "1,2,3,4,5"
    res = parse(istring)
    assert res == [1, 2, 3, 4, 5]
