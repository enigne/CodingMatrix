"""

>>> from hw2 import *

Problem 1

Function: vec_select

>>> D = {'a','b','c'}
>>> v1 = Vec(D, {'a': 1})
>>> v2 = Vec(D, {'a': 0, 'b': 1})
>>> v3 = Vec(D, {        'b': 2})
>>> v4 = Vec(D, {'a': 10, 'b': 10})
>>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
True

Function: vec_sum

>>> D = {'a','b','c'}
>>> v1 = Vec(D, {'a': 1})
>>> v2 = Vec(D, {'a': 0, 'b': 1})
>>> v3 = Vec(D, {        'b': 2})
>>> v4 = Vec(D, {'a': 10, 'b': 10})
>>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
True

Function: vec_select_sum

>>> D = {'a','b','c'}
>>> v1 = Vec(D, {'a': 1})
>>> v2 = Vec(D, {'a': 0, 'b': 1})
>>> v3 = Vec(D, {        'b': 2})
>>> v4 = Vec(D, {'a': 10, 'b': 10})
>>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
True

Problem 2

>>> v1 = Vec({1,2,3}, {2: 9})
>>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
>>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
True


Problem 3

>>> from GF2 import one
>>> D = {'a', 'b', 'c'}
>>> L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
>>> len(GF2_span(D, L))
4
>>> Vec(D, {}) in GF2_span(D, L)
True
>>> Vec(D, {'b': one}) in GF2_span(D, L)
True
>>> Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
True
>>> Vec(D, {x:one for x in D}) in GF2_span(D, L)
True



"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()




