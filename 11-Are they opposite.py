'''
------Instructions------

Task
Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result should be a boolean value, instead of a string.

The opposite means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string. Also take note of the edge case - if both strings are empty then you should return false/False.

Examples (input -> output)
"ab","AB"     -> true
"aB","Ab"     -> true
"aBcd","AbCD" -> true
"AB","Ab"     -> false
"",""         -> false





------Test Cases------
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65]
[0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50]
[1]),[1,0]
[-1]),[0,-1]
[0,0,0,0,0,0,0,0,0]),[0,0]
[]),[]




------Siolution------
'''
def is_opposite(s1,s2):
    if not s1 and not s2:
        return False
    if len(s1) != len(s2):
        return False
    
    for i in range(len(s1)):
        if s1[i]==s2[i] or s1[i].lower() != s2[i].lower():
            return False
    
    '''Another Solution
    for a, b in zip(s1, s2):
        if a.lower() != b.lower() or a == b:
            return False

    # zip ===> takes two (or more) iterables (like strings, lists, etc.) and pairs up their elements in order.
    '''


    '''
    Another solution

    def is_opposite(s1, s2):
    if not s1 or len(s1) != len(s2):
        return False
    return all(a != b and a.lower() == b.lower() for a, b in zip(s1, s2))
    
    '''

    return True



# 