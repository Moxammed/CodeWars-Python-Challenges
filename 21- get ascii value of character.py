'''
Get ASCII value of a character.

For the ASCII table you can refer to http://www.asciitable.com/

'''

def get_ascii(ch: str) -> int: 
    # -> int indicates that the function is expected to return an integer.
    #ch: str means the function expects one parameter named ch, and it should be a string (str), specifically a single character.
    return ord(ch) #It returns the ASCII value of that character using Python’s ord() function.
