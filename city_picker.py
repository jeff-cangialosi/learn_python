# Program to help you pick a city to live in

from sys import exit

def east_coast():
    print("Welcome to the East.")


def midwest():
    print("Welcome to the Midwest.")


def west_coast():
    print("Welcome to the West.")


def south():
    print("Welcome to the South.")


def region_picker(speed, quirky_index, neighbor, ocean_index):

    if (speed == "fast"    and quirky_index <= 5 and
        neighbor == "puke" and ocean_index >= 5):
        print("You seem like an East Coast person.")
        print("Let's figure out which East Coast city is for you.")
        east_coast()

    elif ((speed == "medium" or speed == "slow") and
           quirky_index <= 5 and neighbor == "excite" and
           ocean_index < 5):
        print("You seem like a Midwest person.")
        print("Let's figure out which midwestern city is for you.")
        midwest()

    elif ((speed == "medium" or speed == "slow") and
          quirky_index > 5 and ocean_index >= 5):
        print("You seem like a West Coast person.")
        print("Let's figure out which West Coast city is for you.")
        west_coast()

    else:
        print("I don't know where to put you.")
        print("Let's send you to the South.")
        south()


def end(response):
    print("\n", response, "\n", "Good by now.\n")
    exit(0)

def start():

    scale_answers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    print("""
    Greetings my friend!!\n
    This program will help you figure out which US city to live in.
    We just need to ask you a few questions.
    Let's start with three questions to assess your personality.
    """)

    # Question 1 logic
    print("What pace of life do you like in a city (slow, medium, or fast)?")
    choice_1 = input("> ")

    if choice_1 == "slow" or choice_1 == "medium" or choice_1 == "fast":
        speed = choice_1
    else:
        end("You failed to enter an appropriate response.")

    # Question 2 logic
    print("How quirky are you on a scale of 1 to 10? (10 is most quirky)")
    choice_2 = input("> ")

    if choice_2 in scale_answers:
        quirky_index = int(choice_2)
    else:
        end("You failed to enter an appropriate response.")

    # Question 3 logic
    print("Does saying hello to your neighbors excite you or make you want to puke?")
    choice_3 = input("> ")

    if choice_3 == "excite" or choice_3 == "puke":
        neighbor = choice_3
    else:
        end("You failed to enter an appropriate response.")

    # Question 4 logic
    print("How important is being close to an ocean on a scale of 1 to 10? (10 is most important)")
    choice_4 = input("> ")

    if choice_4 in scale_answers:
        ocean_index = int(choice_4)
    else:
        end("You failed to enter an appropriate response.")

    print(f"""\nHere are your initial responses:\n
     City Speed Preference: {speed}
     Your Level of Quirkiness: {quirky_index}
     Reaction to Neighbor: {neighbor}
     Ocean Preference: {ocean_index}
     """)

    region_picker(speed, quirky_index, neighbor, ocean_index)

start()
