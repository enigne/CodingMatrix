## Task 2

def dict2list(dct, keylist): return [ dct[x] for x in keylist]

def list2dict(L, keylist): return { key:value for (key,value) in zip(keylist,L)} 
## Task 3
def listrange2dict(L):
	return {i:L[i] for i in range(len(L))}
