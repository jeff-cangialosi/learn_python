# Program to help you pick a city to live in

from sys import exit

#def region_picker(speed, quirky, neighbor, ocean)

#def midwest():

#def west_coast():

#def east_coast():

#def south():

def end(reason):
    print(reason, "Good by now.")
    exit(0)

def start():

    scale_answers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    print("""
    Greetings my friend!!\n
    This program will help you figure out which US city to live in.
    We just need to ask you a few questions.
    Let's start with four questions to assess your personality.
    """)

    # Question 1 logic
    print("What pace of life do you like in a city (slow, medium, or fast)?")
    choice_1 = input("> ")

    if choice_1 != "slow" and choice_1 != "medium" and choice_2 != "fast":
        print("Let's try that again. Enter 'slow', 'medium', or 'fast'.")
        choice_1 = input("> ")
    else:
        speed = choice_1

    # Question 2 logic
    print("How quirky are you on a scale of 1 to 10? (10 is most quirky)")
    choice_2 = input("> ")

    if choice_2 in scale_answers:
        ocean_index = int(choice_2)
    else:
        end("Man, learn to type a number.")

    # Question 3 logic
    print("Does saying hello to your neighbors excite you or make you want to puke?")
    choice_3 = input("> ")

    if choice_3 != "excites" and choice_3 != "puke":
        print("That makes no sense. It's easy: excites or puke! Try again.")
        choice_3 = input("> ")

        if

    else:
        choice_3 = neighbor

    # Question 4 logic
    print("How important is being close to ocean on a scale of 1 to 10? (10 is most important)")
    choice_4 = input("> ")

    if choice_4 in scale_answers:
        ocean_index = int(choice_4)
    else:
        end("Man, learn to type a number.")

    return speed, quirky_index, neighbor, ocean_index

start()
