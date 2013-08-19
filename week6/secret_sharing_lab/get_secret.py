import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent
from matutil import rowdict2mat

## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def randVec(): return list2vec([randGF2() for i in range(len(a0.D))])


indep_flag = False
a = [a0 for i in range(5)]
b = [b0 for i in range(5)]

while not indep_flag:
    for i in range(1,5):
        a[i] = randVec()
        b[i] = randVec()
    indep_flag = True
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5): 
                if not is_independent([a[i],a[j],a[k],b[i],b[j],b[k]]): 
                    indep_flag = False
                    break

print(rowdict2mat(a))
print(rowdict2mat(b))

