'''
------Instructions------

Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).
If they are, change the array value to a string of that vowel.
input [100,100,116,105,117,121]=>[100,100,116,"i","u",121] output Return the resulting array.



------Test Cases------'
([118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ], [118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ]),
(["e",121,110,113,113,103,121,121,"e",107,103 ], [101,121,110,113,113,103,121,121,101,107,103 ]),
([118,103,110,109,104,106 ], [118,103,110,109,104,106 ]),
([107,99,110,107,118,106,112,102 ], [107,99,110,107,118,106,112,102 ]),
([100,100,116,"i","u",121 ], [100,100,116,105,117,121 ])
 

 

------Siolution------
'''

def is_vow(inp):
    newArray=[]
    for i in inp:
        if chr(i) in 'aeiou':  # see if the character can be found in the alphabet list
            newArray.append(chr(i)) # Add an element to an array
        else:
            newArray.append(i)
        
    return newArray