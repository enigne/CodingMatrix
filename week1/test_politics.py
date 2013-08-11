"""

>>> from politics_lab import *

Task 1

>>> create_voting_dict()['Clinton']
[-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]


Task2

>>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
>>> policy_compare('Fox-Epstein','Ravella', voting_dict)
-2

Task 3

>>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
>>> most_similar('Klein', vd)
'Fox-Epstein'

Task 4

>>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
>>> least_similar('Klein', vd)
'Ravella'

Task 5

>>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
>>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
-0.5

Task 6

>>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
>>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
[-0.5, -0.5, 0.0]

Task 8
>>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
>>> bitter_rivals(voting_dict)
('Fox-Epstein', 'Ravella')


"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
