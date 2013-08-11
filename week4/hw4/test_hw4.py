"""
>>> from hw4 import *
>>> from vecutil import *


Problem 13

>>> a0 = Vec({'a','b','c','d'}, {'a':1})
>>> a1 = Vec({'a','b','c','d'}, {'b':1})
>>> a2 = Vec({'a','b','c','d'}, {'c':1})
>>> rep2vec(Vec({0,1,2}, {0:2, 1:4, 2:6}), [a0,a1,a2]) == Vec({'a', 'c', 'b', 'd'},{'a': 2, 'c': 6, 'b': 4, 'd': 0})
True

Problem 14

>>> a0 = Vec({'a','b','c','d'}, {'a':1})
>>> a1 = Vec({'a','b','c','d'}, {'b':1})
>>> a2 = Vec({'a','b','c','d'}, {'c':1})
>>> vec2rep([a0,a1,a2], Vec({'a','b','c','d'}, {'a':3, 'c':-2})) == Vec({0, 1, 2},{0: 3.0, 1: 0.0, 2: -2.0})
True

Problem 15

>>> a0 = Vec({'a','b','c','d'}, {'a':1})
>>> a1 = Vec({'a','b','c','d'}, {'b':1})
>>> a2 = Vec({'a','b','c','d'}, {'c':1})
>>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
>>> is_superfluous([a0,a1,a2,a3], 3)
True
>>> is_superfluous([a0,a1,a2,a3], 3)
True
>>> is_superfluous([a0,a1,a2,a3], 0)
True
>>> is_superfluous([a0,a1,a2,a3], 1)
False

Problem 16

>>> vlist = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 0})]
>>> is_independent(vlist)
False
>>> is_independent(vlist[:3])
True
>>> is_independent(vlist[:2])
True
>>> is_independent(vlist[1:4])
True
>>> is_independent(vlist[2:5])
True
>>> is_independent(vlist[2:6])
False
>>> is_independent(vlist[1:3])
True
>>> is_independent(vlist[5:])
True

Problem 17

Problem 18

>>> S = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]]
>>> A = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]]
>>> z = list2vec([0,2,1,1])
>>> exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0})
True


"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
