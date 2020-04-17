# Exercise 21

# Asking for 4 input values
num1 = input("Please enter a number: ")
num2 = input("Please enter another number:")
num3 = input("Please enter another number: ")
num4 = input("Last time! Please enter another number: ")

# Taking all my inputted values and converting them to floating point numbers
# The input comes in as strings so need to convert to use in the functions below
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
num4 = float(num4)

# WHen I call this function, I will only see the printed out portion
# Under the hood it is giving me the "return" value though, which I can assign to a variable
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b     # Any line that runs this is able to assign a + b to a variable

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("\nLet's do some math with just functions!\n")

# In each of these lines, I get the print from the function
# The return value of the function is also assigned to the variables below
age = add(num1, num2)
height = subtract(num2, num3)
weight = multiply(num3, num4)
iq = divide(num4, num1)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("\nHere is a puzzle.\n")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("\nThat became: ", what, "Can you do it by hand?\n")

# Here is my own little formula
# I will use the functions to do this: (88 + 4) / 10 * 3
value_jc = multiply(divide(add(88, 4), 10), 3)
print("Here is the value: ", round(value_jc, 2))
