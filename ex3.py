# This is a string with some text.


print("I will now count my chickens.")

# We have a string of text followed by a calculation.
# We divide 30 by 6 and then add 25 to get 30.
print("Hens", float(25 + 30 / 6))
# Due to order of operations we start by multiplying 25 *3, giving us 75.
# Then move onto the modulo (%). 75 % 4 is 3 (the remainder of dividing 75 by 4 is 3).
# Finally, do 100 - 3 to get 97.
print("Roosters", float(100 - 25 * 3 % 4))

# Nice little string here again.
print("Now I will count the eggs:")

# Do the modulo first, resulting in 0. Then divide 1/4 to get 0.25.
# We are left with 3 + 2 + 1 - 5 - 0.25 + 6. We get 6.75.
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# We have a string with text. The calculations will not run here.
print("Is it true that 3 + 2 < 5 - 7?")

# This is going to run as a TRUE/FALSE statement and return FALSE
print(float(3 + 2) < float(5 - 7))

# String followed by a numeric calculation.
print("What is 3 + 2?", float(3 + 2))
# String followed by a numeric calculation.
print("What is 5 - 7?", float(5.57676 - 7.3))

# This is a string.
print("How about some more?")

# String followed by a Boolean TRUE/FALSE statement
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
