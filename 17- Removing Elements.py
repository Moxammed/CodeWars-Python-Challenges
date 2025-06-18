'''
Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!

'''

def remove_every_other(my_list):
    return my_list[::2]


'''
Explanation:
my_list[::2] uses list slicing to return every second element starting from index 0.

The syntax is:
start:stop:step → ::2 means "start at 0, go to end, step by 2".
'''