'''
------Instructions------

Create a method that takes as input a name, city, and state to welcome a person. Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.

Example:

['John', 'Smith'], 'Phoenix', 'Arizona'
This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!'
'''



#------Solution------
def say_hello(name, city, state):
    names =""
    for i in name:
        names+=" "+i
    
    return f"Hello,{names}! Welcome to {city}, {state}!"
