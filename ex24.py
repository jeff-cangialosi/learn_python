# This is a basic string
print("Let's practice everything.")
# The \ allows you to throw a single ' without breaking the string
# The \\ actually returns one | and doesn't throw an escape (basically just writes a backslash)
print('You\'d need to know \'bout escapes with \\ that do:')
# Using new line and tab here
print('\n newlines and \t tabs.')

# Using triple quotes to write a poem in paragraph format
# The last line gets a new line and two tabs
# Poem is a variable. You need to run a print function below to actually see it
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)     # Printing out the poem variable defined above
print("--------------")


# Doing math within a variable
five = 10 - 2 + 3 - 6
# Using an f-string here to include a variable within a string
print(f"This should be five: {five}")

# Writing a function called secret formula that will take one argument 'started'
# The function will return three values
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# Creating a new variable called start_point
start_point = 10000
# This is going to work like argvs! Unpacking the function output to 3 variables
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))

# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to format a string
# the *formula is a little confusing!!
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
