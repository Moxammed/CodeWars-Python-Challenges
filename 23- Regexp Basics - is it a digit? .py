'''
------Instructions------

Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a single digit (0-9), false otherwise.


  
------Solution------
'''

def is_digit(n):
    return isinstance(n, str) and len(n)==1 and n.isdigit()
#     return isinstance(n, int) ==> if the instance was int
#     return isinstance(n, (int,float)) ==> if the instance was int or float
#     return n.isdigit() ===> if the instance was digit either in number form or string forms