from hw3 import *
from vec import Vec
from mat import Mat
from tester_classes import VecTester
from submit_hw3 import *

f = dot_product_mat_vec_mult
d1 = {0, 1, 2, 3, 4}
d2 = {'a','b','c','d'}
D1 = (d1, d2)
M1 = Mat(D1, {(3, 'd'): 27, (1, 'c'): 26, (3, 'c'): 35, (3, 'a'): 20, (4, 'd'): 26, (1, 'd'): 5, (2, 'a'): 50, (2, 'b'): 11, (1, 'a'): 27, (2, 'c'): 34, (2, 'd'): 40, (4, 'a'): 33, (0, 'b'): 31}) 
M2 = Mat(D1, {(0, 'c'): 1, (3, 'd'): 2, (1, 'c'): 1, (0, 'a'): 1, (3, 'b'): 2, (1, 'b'): 2, (4, 'd'): 2, (1, 'd'): 2, (2, 'a'): 0, (2, 'b'): 2, (0, 'd'): 1, (2, 'c'): 2, (4, 'c'): 0, (4, 'a'): 1, (0, 'b'): 0})
M3 = Mat(D1, {(0, 'a'): 3, (4, 'd'): 4, (3, 'a'): 5, (2, 'a'): 5, (0, 'd'): 1, (1, 'a'): 3, (4, 'b'): 4, (2, 'c'): 3, (0, 'b'): 4, (3, 'b'): 5, (4, 'a'): 3, (2, 'd'): 3, (4, 'c'): 5})
M4 = Mat(D1, {(0, 'c'): 0, (3, 'c'): 2, (1, 'b'): 0, (4, 'd'): 2, (3, 'a'): 1, (1, 'd'): 1, (2, 'b'): 2, (2, 'a'): 2, (0, 'd'): 2, (1, 'a'): 0, (2, 'c'): 0, (4, 'c'): 0, (3, 'b'): 0, (3, 'd'): 1, (0, 'b'): 1})
V1 = Vec(d2, {'b': 12, 'c': 0, 'a': 2, 'd': 6})
V2 = Vec(d2, {'b': 19, 'c': 19, 'a': 19, 'd': 3})
V3 = Vec(d2, {'b': 18, 'c': 19})
matrices = [M1, M2, M3, M4]
vectors  = [V1, V2, V3]
results = []
V_test = VecTester(d2)
_ = f(M1, V_test)
results.append(sorted(V_test.left+V_test.right, key=tf))
V_test = VecTester(d2)
_ = f(M2, V_test)
results.append(sorted(V_test.left+V_test.right, key=tf))
V_test = VecTester(d2)
_ = f(M3, V_test)
results.append(sorted(V_test.left+V_test.right, key=tf))
V_test = VecTester(d2)
_ = f(M4, V_test)
results.append(sorted(V_test.left+V_test.right, key=tf))



