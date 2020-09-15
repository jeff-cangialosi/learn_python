# Exercise 6
# This was written listening to the Hamilton soundtrack

# Creating some variables with a numeric and then a string
types_of_people = 10
x = f"There are {types_of_people} types of people."

# Creating 3 variables with the last value including an f string
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# Printing f strings using the newly created variables x and y
print(f"I said: {x}")
print(f"I also said: '{y}'")

# A variable with a boolean value
hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

# Using .format here so that we can add something to a previously created string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
