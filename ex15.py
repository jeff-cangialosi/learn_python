# Exercise 15

# Importing the module sys to use the feature argv
from sys import argv

# Unpacking argv into two variables
script, filename = argv

# Creating a variable named txt and defining it with by calling the fucntion open on filename
txt = open(filename)

# F-string with a little message about filename
print(f"Here's your file {filename}.")
# Calling the function read on the variable txt
print(txt.read())

# Doing the same thing as above but using an input function to get the file
print("Type the filename again:")
# Creating new variable called file_again
file_again = input("> ")

# Calling the open function on file_again
txt_again = open(file_again)

# Calling the read function on txt_again
print(txt_again.read())
