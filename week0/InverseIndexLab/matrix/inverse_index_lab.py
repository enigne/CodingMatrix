from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,2)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    dicmap = {}
    for par in list(enumerate(strlist)):
        doc_id = par[0]
        strsplit = par[1].split()
        for word in strsplit:   
            if not word in dicmap.keys():
                dicmap[word] = set();
            dicmap[word].add(doc_id);
    return dicmap

## Task 5
def orSearch(inverseIndex, query):
    result = set()
    for word in query:
        if word in inverseIndex.keys():
            result = result | (inverseIndex[word])
    return result

## Task 6
def andSearch(inverseIndex, query):
    result = set()
    firstTimeflag = True
    for word in query:
        if word in inverseIndex.keys():
            if firstTimeflag:
                result = result | (inverseIndex[word])
            else:
                result = result & (inverseIndex[word])
            firstTimeflag = False
    return result
