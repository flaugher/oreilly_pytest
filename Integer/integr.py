#!/usr/bin/env python
from pdb import set_trace as debug

def parse(istring):
    """
    Inputs:
    istring like "1,3,5,9"

    Outputs:
    list containing istring like "[1, 3, 5, 9]"
    """
    ilist = []
    for i in istring.split(","):
        ilist.append(int(i))
    return ilist

if __name__ == '__main__':
    ilist = parse("1,3,5,9")
    print(ilist)
