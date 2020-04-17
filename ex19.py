# Exercise 19

# Defining a function called cheese_and_crackers
# The function takes two inputs and returns 4 lines of strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")     # The \n gives us a line spacing in the output


# Passing two numerics into the function as inputs
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# You calso apparently just throw strings in as your inputs as well
print("Now we are testing if we can input strings.")
cheese_and_crackers("LOTS", "MINIMAL")
print("Apparently this works too!\n")

# Defining two variables that we are then going to pass to the function cheese_and_crackers
print("OR, we can use the variables from our script:")
amount_of_cheese = 15
amount_of_crackers = 60

# Running the function with the two variables defined above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Doing math within the two input slots of our function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


# Putting it all together and using the combination of math and variables for inputs
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Creating a second function within this exercise
# This function takes in numbers and returns some values
def city_pop(milwaukee, chicago, cleveland):
    print(f"The population of Milwaukee is {milwaukee}.")
    print(f"The population of Chicago is {chicago}.")
    print(f"The population of Cleveland is {cleveland}.")
    print("The combined population of all these cities is: ", milwaukee + chicago + cleveland, "\n")

print("Let's input the actual city population totals directly.")
city_pop(595000, 2716000, 386000)

# Creating city variables with population amount assigned
milwaukee = 595000
chicago = 2716000
cleveland = 386000

print("Using my new variables to return the city population figures.")
city_pop(milwaukee, chicago, cleveland)

print("Let's use math now.")
city_pop(100 + 5000, 5000 / 2, 10000)

# I thought that throwing strings in the function might break it because of the additive operator at the end of the functions
# The function did not break though. It just concatenated the strings. That's cool.
print("Let's throw in some strings now.")
city_pop("600k", "2.7mm", "350k")

# Using input() within the function to get inputs to pass into the function
city_pop(int(input()), int(input()), int(input()))







# hey hey hey
