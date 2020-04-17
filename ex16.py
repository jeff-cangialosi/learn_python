# Exercise 16

from sys import argv

script, filename = argv

# F-string putlling in the variable filename
print(f"We're going to erase {filename}.")
# Printing two lines of strings with instructions
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Soliciting an input to do something to filename
input("?")

# Opening filename and creating a new variable called target
print("Opening the file...")
target = open(filename)

# Erasing the contents of filename
print("Truncating the file. Goodbye!")
target.truncate()

# Simple string
print("Now I'm going to ask you for three lines.")

# Creating 3 new variables and defining them with inputs
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

# Writing the string content of the variables into the file
target.write(line1 + "\n" + line2 + "\n" + line3)

# Closing the file afrer we've written to it
print("And finally, we close it.")
target.close()

print("Now let's do this again.\nI'm opening up the file to see what's inside.")
target_a = open(filename)

print(target_a.read())

print("""
Shall we close it back up again?
Hit enter if yes and ^C if no.
Thanks boss!
""")

input("? ")

target_a.close()
