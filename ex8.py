# Exercise 8

# Variable called formatter with 4 input brackets
formatter = "{} {} {} {}"

# Just taking a look at formatter
print(formatter)

# Using format to fill the 4 input brackets in variable formatter
print(formatter.format(1, 2, 3, 4))

# Using format to fill the 4 input brackets within the variable formatter with new values
print(formatter.format("one", "two", "three", "four"))

# We now throw some Boolean values into formatter
print(formatter.format(True, False, False, True))

# Throwing formatter into itself here to get a ton of brackets
print(formatter.format(formatter, formatter, formatter, formatter))

# Throwing text strings into formatter
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
