"""
>>> from hw6 import *
>>> from vecutil import *

Problem 2

>>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
True
>>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
False
>>> is_echelon([[2,1,0],[0,1,0],[0,0,1]])
True
>>> is_echelon([[2,1,0],[-4,0,0],[0,0,1]])
False
>>> is_echelon([[2,1,0],[0,3,0],[1,0,1]])
False
>>> is_echelon([[1,1,1,1,1],[0,2,0,1,3],[0,0,0,5,3]])
True

Problem 5

>>> D = {'A','B','C','D','E'}
>>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
>>> b_list = [one,0,one]
>>> cols = ['A', 'B', 'C', 'D', 'E']
>>> echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
True

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
