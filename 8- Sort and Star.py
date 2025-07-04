

'''
------Instructions------

You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.
The returned value must be a string, and have "***" between each of its letters.
You should not remove or add elements from/to the array.




------Test Cases------'
 (["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]), 'b***i***t***c***o***i***n' )
 (["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]), 'a***r***e')
 (["lets", "talk", "about", "javascript", "the", "best", "language"]), 'a***b***o***u***t')
 (["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]), 'c***o***d***e')
 (["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]), 'L***e***t***s')

 

 

------Solution------
'''
def two_sort(array):
    sorted_array = sorted(array)       
    first_word = sorted_array[0]   
    
    return '***'.join(first_word)        