'''
------Instructions------

Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.

Examples:

Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3]


  
------Solution------
'''

def distinct(seq):
    result =[]
    [result.append(x) for x in seq if x not in result] # I love this line of code
    return result