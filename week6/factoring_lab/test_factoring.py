"""
>>> from factoring_lab import *

Task 1

>>> int2GF2(3)
one
>>> int2GF2(100)
0

Task 2

>>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
True





"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
