# Exercise 5
# This was coded while listening to the Hamilton soundtrack

name = 'Jeff Cangialosi'
age = 29 # this is now a high number
height = 70 # inches
weight = 170 # lbs
height_cm = round(height * 2.54, 0)
weight_kg = round(weight * 0.453592, 3)
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall. If we convert that to centimeters, that's {height_cm} centimeters.")
print(f"He's {weight} pounds heavy. If we convert that to kilograms, that's {weight_kg} kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
