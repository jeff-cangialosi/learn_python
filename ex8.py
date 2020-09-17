# Exercise 8

# Creating a variable called formatter that can take 4 arguments
formatter = "{} {} {} {}"

# You get thrown an error if you provide less than 4 arguments
# I experimented throwing 5 arguments here, and the fifth argument is ignored
print(formatter.format(1, 2, 3, 4, 5))

# Throwing string arguments
print(formatter.format("one", "two", "three", "four"))

# Throwing booleans and a string argument into formatter
print(formatter.format(True, False, False, "Butterfly"))

# This is meta - throwing a variable back into itself
print(formatter.format(formatter, formatter, formatter, formatter))

# This all prints on one line. The interpreter does not care about the line breaks.
# This is still read as a list of strings
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear",
    "Or even a song about deer" # this line does not show up (fifth arg)
))
