#!/usr/bin/env python
from block import Amount

# Run: cd block; PYTHONPATH=. pytest

def test_amount_todict():
    a = Amount('matt', 5)
    res = a.todict()
    assert res == {'uuid': 'matt', 'amount': 5}
