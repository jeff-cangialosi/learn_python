print("""\nI'd like to know who you think the MVP should be in the NBA.
There are a few obvious choices for the 2019-2020 season, but let's see who
you decide on. Please enter the first name of your MVP pick.\n""")

mvp_pick = input("> ")

if mvp_pick == "Lebron":
    print("So your choice is King James - always a solid pick.")
    print("Let me ask you another  question then.")
    print("Should King James have stayed on the Cavaliers?")
    print("1. Yes")
    print("2. No")

    lebron = input("> ")

    if lebron == "1":
        print("Cool. I agree. He should have stayed in his home town.")
    elif lebron == "2":
        print("So you're a Lakers fan. I guess that's alright.")
    else:
        print("Dude, it was a yes or no question. Why did you answer something different?")

elif mvp_pick == "Giannis":
    print("I love this pick. This is my choice too!")

elif mvp_pick == "James":
    print("By entering James, I assume you mean James Harden.")
    print("Is that correct?")
    print("1. Yes")
    print("2. No")

    harden = input("> ")

    if harden == "1":
        print("Nice. That's what I thought.")
    else:
        print("Sorry dude. I'm not sure what player you're thinking of.")

else:
    print("You didn't pick Lebron James, Giannis, or James Harden.")
    print(f"Instead, you said the MVP is {mvp_pick}.")
    print("I'm not sure I agree, but I look forward to hearing your case.")
