from inverse_index_lab import makeInverseIndex,orSearch,andSearch
stories = list(open("stories_small.txt"))
idx = makeInverseIndex(stories)
re = orSearch(idx,['travelers', 'use', 'Baltimore', 'major-league', 'whether'])
re1 = andSearch(idx, ['the', 'in', 'use', 'times'])
re2 = andSearch(idx, ['made', 'are'])
