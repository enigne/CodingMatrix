from politics_lab import *
voting_dict = create_voting_dict()
a = 'Chafee'
b = 'Santorum'

ms = most_similar(a, voting_dict)
ls = least_similar(b, voting_dict)

print(ms)
print(ls)
