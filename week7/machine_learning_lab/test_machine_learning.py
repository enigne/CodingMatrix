"""
>>> from machine_learning_lab import *


Task 1

>>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
True


"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
