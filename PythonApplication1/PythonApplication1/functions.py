import time
class functions:
    
    def print_choices(choiceA, choiceB, choiceC, choiceD):
        print("---Make a choice---\n")
        time.sleep(2)
        print('  A. ' + choiceA)
        time.sleep(1)
        print('  B. ' + choiceB)
        time.sleep(1)
        print('  C. ' + choiceC)
        time.sleep(1)
        print('  D. ' + choiceD)
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

    def choice_result(choice, resulta, statusa, resultb, statusb, resultc, statusc, resultd, statusd):
        if choice == 'a':
            print(resulta + "\n")
            return statusa
        elif choice == 'b':
            print(resultb + "\n")
            return statusb
        elif choice == 'c':
            print(resultc + "\n")
            return statusc
        elif choice == 'd':
            print(resultd + "\n")
            return statusd
        time.sleep(4)

    def game_exit():
        print("The game is over. Please proceed with reality.")



