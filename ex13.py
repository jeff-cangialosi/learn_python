# Exercise 13

# Importing a module here to use the feature argv
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

# Each of these lines prints a text string and then ends with a variable assigned by argv above
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# This is a simple input setup to have a user provide data while the script is running
x = input('Do you like this script? ')
print("You answered:", x)
