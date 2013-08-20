from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

import echelon

## Ungraded Task
def root_method(N):
    a = intsqrt(N) + 1
    b = intsqrt(a**2-N)
    while (abs(a**2-b**2- N) > 1e-9):
        a += 1
        b = intsqrt(a**2-N)
    return (a+b,a-b)   



## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    return one if i % 2 else 0

## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset,{key:int2GF2(value) for (key,value) in factors})

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    roots = []
    rowlist = []
    count = 0
    x = intsqrt(N) + 2
    while count < len(primeset)+1 :
        factor_list = dumb_factor(x**2-N, primeset)
        if len(factor_list) > 0 :
            count += 1
            rowlist.append(make_Vec(primeset,factor_list))
            roots.append(x)
        x += 1
    return (roots, rowlist)



## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    alist = [roots[ele] for ele in range(len(roots)) if v[ele] != 0]
    a = prod(alist)
    c = prod([x**2-N for x in alist])
    b = intsqrt(c)
    assert b**2 == c
    return (a,b)


## Task 5
N = 2461799993978700679
primelist = primes(1000)
(roots,rowlist) = find_candidates(N, primelist)
M = echelon.transformation_rows(rowlist)

sm = N
for i in range(len(M)-1,90,-1):
    (a,b) = find_a_and_b(M[i],roots,N)
    factor = gcd(a-b,N)
    sm = factor if factor < sm and factor > 1 else sm

smallest_nontrivial_divisor_of_2461799993978700679 = sm 
