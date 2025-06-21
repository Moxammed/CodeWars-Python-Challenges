'''
------Instructions------

In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.

Examples:

[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []


  
------Solution------
'''

def two_highest(arg1):
    if not arg1:
        return []
    
    unique = list(set(arg1)) # remove duplicates and makes the list ascending
    unique=sorted(unique, reverse=True) # sort in descending order. make sure the last thing you do the sort.
    
    return unique[:2]
    