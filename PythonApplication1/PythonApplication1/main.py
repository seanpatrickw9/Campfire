# Text-based adventure game with multiple plot lines.
# Sean Wallace - August 17th 2018
import time
from functions import functions
game_over = False

while game_over == False:
        
    print("Welcome to CAMPFIRE!\nYou have grown weary of the everyday stresses of urban life.\n" + \
    "You decided to take some time off and go camping in the vast wilderness.\n\n")

    start = input("Press Enter to continue...")

    print("Day 1 - 5:30PM \n")
    time.sleep(2)
    print("You had a late start today, but you finally managed to setup camp.")
    time.sleep(4)
    print("It's a pretty nice spot! You found a plateau that overlooks a small lake.\n")
    time.sleep(4)
    print("You decide to get up, have a stretch, and take in the beautiful scenery. \n")
    time.sleep(4)

    #Decision1#
    functions.print_choices("Yell, Im the king of the world", "Howl", "Kick a rock", "Drink an Angry Orchard and get lit.")
    choice = functions.choose_choice()
    game_over = functions.choice_result(choice, "Whatever, your highness", False,\
       "You start to grow hair in places hair hasn't grown before",\
        False, "You scuff your shoes", False, "There's only Bud Lite",False)
    if game_over:
        functions.game_exit()
        break

    print("You take a deep breath and suddenly feel intoxicated by the fresh mountain air.\n" +\
    "It's getting late, and you've a had a full day of traveling and setting up.")
    time.sleep(4)

    #Decision2#
    functions.print_choices("Start a fire. Read some manga.", "Go explore the wilderness before bed.",\
                            "Gather firewood near camp.","Grab your bow and arrows and hunt some food.")
    choice = functions.choose_choice()
    game_over = functions.choice_result(choice,"Good job, nerd", False,"You got eaten by a bear",True,\
        "You got firewood AND edible berries!",False, "You killed a deer...monster",False)
    if game_over:
        functions.game_exit()
        break
        
    print("Thanks for playing the demo!")
    game_over = True