'''
Challenge:
Ahoy Matey!
Welcome to the seven seas.
You are the captain of a pirate ship.
You are in battle against the royal navy.
You have cannons at the ready.... or are they?
Your task is to check if the gunners are loaded and ready, if they are: Fire!
If they aren't ready: Shiver me timbers!
Your gunners for each test case are 2, 3 or 4.
When you check if they are ready their answers are in a dictionary and will either be: aye or nay
Firing with less than all gunners ready is non-optimum (this is not fire at will, this is fire by the captain's orders or walk the plank, dirty sea-dog!)
If all answers are 'aye' then Fire! if one or more are 'nay' then Shiver me timbers!
Also, check out the new Pirates!! Kata: https://www.codewars.com/kata/57e2d5f473aa6a476b0000fe



Test Cases:
a = {'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}
b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}
c = {'Joe':'nay','Johnson':'nay','Peter':'aye'}
d = {'Mike':'nay','Joe':'nay','Johnson':'nay','Peter':'nay'}



Solution:
'''
def cannons_ready(gunners):
    for i in gunners:
        if gunners[i]=="nay":
            return "Shiver me timbers!"
    return "Fire!"