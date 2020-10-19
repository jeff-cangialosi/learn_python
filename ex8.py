# Exercise 8

# Creating a variable called formatter that takes 4 arguments
formatter = "{} {} {} {}"

# Each of these print statements is throwing 4 arguments into formatter
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your\n",
    "Own text here\n",
    "Maybe a poem\n",
    "Or a song about fear"
))
