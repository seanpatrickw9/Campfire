# Text-based adventure game with multiple plot lines.
# Sean Wallace - August 17th 2018
import time

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
print("---Make a choice---\n")
time.sleep(2)
print('  A. Yell, "I'+ "'" + 'm the king of the world!"')
time.sleep(1)
print('  B. Howl.')
time.sleep(1)
print('  C. Kick a rock over the edge of the plataue.')
time.sleep(1)
print('  D. Crack open an Angry Orchard and start getting lit.')
time.sleep(2)

def choose_choice():
    inloop = True
    while inloop == True:
        choice = input("Choice: ")
        choice = choice.lower()

        if choice != 'a' and choice != 'b' and choice != 'c' and choice != 'd':
            continue
        else:
            break
    return choice

choice = choose_choice()
if choice == 'a':
    print("Considering there's no one within a 50 mile radius to contest you, you get the crown your highness.\n")
elif choice == 'b':
    print("After letting that out, you notice a small chest air protrude from the neck whole of your shirt.\n" +\
          "You decide to pluck it, then let out another howl.\n")
elif choice == 'c':
    print("You scuff your shoe. You still have the nicest shoes at the campsite though.\n")
elif choice == 'd':
    print("Shit! There's only Bud Lite.\n")

time.sleep(4)
print("You take a deep breath and suddenly feel intoxicated by the fresh mountain air.\n" +\
    "It's getting late, and you've a had a full day of traveling and setting up.")
time.sleep(6)

print("---Make a choice---\n")
time.sleep(2)
print('  A. Start a fire. Read some manga.')
time.sleep(1)
print('  B. Go explore the wildnerss before bed.')
time.sleep(1)
print('  C. Gather firewood near camp.')
time.sleep(1)
print('  D. Grab your bow and arrows and hunt some food.')
time.sleep(1)
choice = choose_choice()
if choice == 'a':
    print("You read some 'Zobebobe Girl', but it doesn't take long before your eyes start getting heavy.\n" + \
        "You bring yourself to get up, put out the fire, and crawl into your sleeping bag.\n" + \
        "Your stomach rubmles...")
elif choice == 'b':
    print("You venture out unprepared. A bear finds you and makes minced meat out of you. Congratulations!\n" +\
          "For the next few days you'll be traveling the its gatrointestinal tract.\n")
elif choice == 'c':
    print("You've gathered plenty of firewood for the coming days, and even managed to find some edible berries!\n")
elif choice == 'd':
    print("You managed to track down a deer. You inhale slowly as you draw back the bowstring, focus on the targeting \n" + \
        "the deers heart, and exhale as you release....")
    time.sleep(3)
    print("Direct hit!!!")
    time.sleep(1)
    print("You carry it's carcus to camp and have yourself of grand feast")

time.sleep(4)
print("Thanks for playing the demo!")




