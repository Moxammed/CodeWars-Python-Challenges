'''
------Instructions------

Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


------Test Cases------'
  even_or_odd(1), "Odd"
  even_or_odd(2) should return "Even"'
  even_or_odd(-1) should return "Odd"'  
  even_or_odd(-2) should return "Even"'
  even_or_odd(0) should return "Even"'
 

------Solution------
'''


def even_or_odd(number):
    return "Even" if number%2==0 else "Odd"

