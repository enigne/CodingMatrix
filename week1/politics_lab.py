voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    voting_dict = {}
    for i in range(len(voting_data)):
        temp = voting_data[i].split();
        voting_dict[temp[0]] = [int(temp[i]) for i in range(3,len(temp))]
    return voting_dict
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    
    return sum([voting_dict[sen_a][i]*voting_dict[sen_b][i] for i in range(len(voting_dict[sen_a]))])


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
   
    simi_dict = {k:policy_compare(sen,k,voting_dict) for k in voting_dict.keys() if k != sen}
    return max(simi_dict, key=simi_dict.get)
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """

    simi_dict = {k:policy_compare(sen,k,voting_dict) for k in voting_dict.keys() if k != sen}
    return min(simi_dict, key=simi_dict.get)
    
    

## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    simi_dict = {k:policy_compare(sen,k,voting_dict) for k in voting_dict.keys() if k != sen and k in sen_set}

    return sum(simi_dict.values())/len(simi_dict.keys())

most_average_Democrat = ... # give the last name (or code that computes the last name)


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    average_record = []
    for i in range(len(list(voting_dict.values())[0])):
        temp_record = [voting_dict[senator][i] for senator in sen_set]
        average_record.insert(i,  sum(temp_record)/len(temp_record))
    return average_record

voting_dict = create_voting_dict()
Democrat_set = [voting_data[i].split()[0] for i in range(len(voting_data)) if voting_data[i].split()[1]=='D']
average_Democrat_record = find_average_record(Democrat_set, voting_dict) # (give the vector)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    first_senator = list(voting_dict.keys())[0];
    disagree_argument = policy_compare(first_senator, first_senator, voting_dict)
    most_disagree1 = list(voting_dict.keys())[0];
    most_disagree2 = list(voting_dict.keys())[0];
    
    for senator1 in voting_dict.keys():
        for senator2 in voting_dict.keys():
            temp_record = policy_compare(senator1, senator2, voting_dict) 
            if temp_record < disagree_argument:
                disagree_argument = temp_record 
                most_disagree1 = senator1
                most_disagree2 = senator2
    return (most_disagree1, most_disagree2)

