# Exercise 6
# This was written listening to the Hamilton soundtrack

# Creating a variable and assigning a numeric to it
types_of_people = 10

# Variable x with an f-string to be able to add a variable in
x = f"There are {types_of_people} types of people."

# Basic variables here assigned to text strings
binary = "binary"
do_not = "don't"

# Have a varibale with another f-string here with two variables implanted
y = f"Those who know {binary} and those who {do_not}."

# Printing the variables x and y here to show their outputs
print(x)
print(y)

# Printing f-strings here with x and y embedded
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assigning the Boolean value of False to a variable named hilarious
hilarious = False

# Created a string here and left an open bracket to allowing it to be formatted
joke_evaluation = "Isn't that joke so funny?! {}"

# Using a .format syntax here - so fancy!!
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# Combining variables with 2 text strings here
print(w + e)
