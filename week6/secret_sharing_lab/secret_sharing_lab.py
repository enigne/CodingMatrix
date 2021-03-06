# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    u = list2vec([randGF2() for i in range(len(a0.D))])
    while (a0*u != s or b0*u != t):
        u = list2vec([randGF2() for i in range(len(a0.D))])
    return u



## Problem 2
# Give each vector as a Vec instance
secret_a0 = a0
secret_b0 = b0
secret_a1 = list2vec([0, one, one, 0, 0, 0])  
secret_b1 = list2vec([one, one, one,0, 0, 0]) 
secret_a2 = list2vec([0, 0, one, 0, one, one]) 
secret_b2 = list2vec([0, one, one, 0, 0, one]) 
secret_a3 = list2vec([one, 0, 0, one, one, 0]) 
secret_b3 = list2vec([one, 0, 0, one, 0, one]) 
secret_a4 = list2vec([0, 0, one, one, one, 0]) 
secret_b4 = list2vec([0, 0, 0, 0, one, 0]) 

