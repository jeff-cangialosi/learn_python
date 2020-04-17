people = 4
cars = 50
trucks = 30


if (cars > people and trucks < cars):
    print("\nWe should take the cars.")
elif cars < people:
    print("\nWe should not take the cars.")
else:
    print("\nWe can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.\n")
else:
    print("Fine, let's stay home then.\n")
