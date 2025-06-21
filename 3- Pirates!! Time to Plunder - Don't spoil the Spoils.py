'''
Ahoy Matey!

If you have succesffully managed your cannon crew and only fired when the cannons were ready then you have won the naval battle. If you haven't, do the Kata here.

What comes after besting dirty sea-dogs? Plundering and the spoils of battle!

Your crew has now collected all the riches from the defeated enemies. You need to make sure the Spoils(rewards/riches) are not spoiled(ruined).

They get spoiled(ruined) if not enough of your crew gets their fair share, or if one or more get too much of a share.

You have 4 inputs:

spoils total - The value of riches plundered (will be int)
expenses - The percentage of the spoils_total, before captain_tax is taken out, that is taken for expenses and ship repairs (i.e. expenses = 5 means 5 percent of total spoils were used for expenses)
captain tax - The amount of money you as captain skim off the top before distributing to your crew
crew - a table of crew members where keys represent their names and values represent the amount of money they took
Crew example:

{
  "Wallace": 25,
  "Jimmy": 23,
  "Petey": 15,
  "George": 12
}
In that above example, Petey and George obviously have less than the others. Or Wallace and Jimmy took more than they should have.

Your task is to take in the array above and determine if each crew member got their fair share. If they didn't then there is either a thief or thieves, or the captain is greedy.

There are three possible outcomes. Here's some examples using the above crew:

If one or more got more than their fair share return the name of the thief or thieves with orders to walk the plank in alphabetical order like so:

"Jimmy, Wallace - Walk the plank!"
If they all got their fair share then everyone is happy:

"Yo-Ho. Yo-Ho. A pirate's life for me!"
If one or more didn't get their fair share, but the rest did (meaning no theives) then that means the missing money is with the Captain. Return the following with the names of the crew members in alphabetical order who lost their fair share.

"Captain needs his gold! Sorry George, Petey"




Test Cases:
crew = {'Wallace': 25,'Jimmy': 23,'Petey':15,'George':12}
test.assert_equals(spoils(100, .05, 20, crew),"Jimmy, Wallace - Walk the plank!")
test.assert_equals(spoils(80, .20, 10, crew),"Jimmy, Petey, Wallace - Walk the plank!")
test.assert_equals(spoils(1000, .1, 2, crew),"Captain needs his gold! Sorry George, Jimmy, Petey, Wallace")

crew = {'Wallace': 5,'Jimmy': 5,'Petey':5,'George':5}
test.assert_equals(spoils(30, .2, 4, crew),"Yo-Ho. Yo-Ho. A pirate's life for me!")



Solution:
'''
def spoils(spoils_total, expenses, captain_tax, crew):
    expense_amount = expenses * spoils_total
    new_total = spoils_total - expense_amount - captain_tax
    fair_share = new_total / len(crew)

    Result = ""
    Names_high_share = []
    Names_low_share = []
    Total_shared = 0
    Shared_equal = 0

    for i in crew:
        if crew[i] > fair_share:
            Names_high_share.append(i)
            Total_shared += crew[i]
        elif crew[i] < fair_share:
            Names_low_share.append(i)
            Total_shared += crew[i]
        else:
            Shared_equal += crew[i]

    if Shared_equal == new_total:
        Result = "Yo-Ho. Yo-Ho. A pirate's life for me!"
    elif Total_shared + Shared_equal == new_total and Names_high_share:
        Names_high_share = sorted(Names_high_share)
        names = ", ".join(Names_high_share)
        Result = names + " - Walk the plank!"
    elif Total_shared + Shared_equal == new_total and Names_low_share:
        Names_low_share = sorted(Names_low_share)
        names = ", ".join(Names_low_share)
        Result = "Captain needs his gold! Sorry " + names
    elif Total_shared + Shared_equal < new_total and Names_low_share and not Names_high_share:
        Names_low_share = sorted(Names_low_share)
        names = ", ".join(Names_low_share)
        Result = "Captain needs his gold! Sorry " + names
    elif Total_shared + Shared_equal < new_total and not Names_low_share and Names_high_share:
        Names_low_share = sorted(Names_low_share)
        names = ", ".join(Names_low_share)
        Result = "Captain needs his gold! Sorry " + names
    elif Total_shared + Shared_equal > new_total and Names_low_share and Names_high_share:
        Names_high_share = sorted(Names_high_share)
        names = ", ".join(Names_high_share)
        Result = names + " - Walk the plank!"

    return Result