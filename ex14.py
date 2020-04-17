# Exercise 14

# Importing the module sys
from sys import argv

# These are the two inputs that need to be entered in the command line
script, user_name, birth_month = argv
prompt = 'Insert answer here: '

# Using the unpacked variables from the argv to create an opening statement for the user
# Also using f-strings here to insert variables into strings
print(f"\nHi {user_name}, I'm the {script} script.")
print(f"I see that you were born in {birth_month}.")
print("I'd like to ask you a few questions.")


# Using an f-string and input() to ask a question
likes = input(prompt)

# Using an f-string and input() to ask a question
print(f"\nWhere do you live {user_name}?")
lives = input(prompt)

# Using a string and input() to ask a question
print("\nWhat kind of computer do you have?")
computer = input(prompt)

# Using triple quotes here to do a multi-line string
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
