# Exercise 5
# This was coded while listening to the Hamilton soundtrack

mb_name = 'Giannis'
mb_age = 25 # I think this is correct
mb_height = 84 # Also a guess but probably close
mb_weight = 260 # Hopefully close
mb_eyes = 'Brown'
mb_teeth = 'White'
mb_hair = 'Black'

print(f"Let's talk about {mb_name}.")
print(f"He's {mb_height} inches tall.")
print(f"He's {mb_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {mb_eyes} eyes and {mb_hair} hair.")
print(f"His teeth are usually {mb_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = mb_age + mb_height + mb_weight
print(f"If I add {mb_age}, {mb_height}, and {mb_weight} I get {total}.")

centi_converter = 2.54

mb_height_cm = mb_height * centi_converter
print(f"Converting the height into centimeters, we get {mb_height_cm}.")
