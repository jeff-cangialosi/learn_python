# This is a simple string of text
print("Mary had a little lamb.")
# This is a formatted string
print("Its fleece was white as {}.".format('snow'))

color = "white"

# Creating an f-string here with the variable color above
print(f"It's fleece was {color}.")

# Simple string with text
print("And everywhere that Mary went.")
print("." * 10) # this will create 10 periods

# Creating a bunch of variables defined with letters
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# the end = '' keeps these two print statements on the same line
print(end1 + end2 + end3 + end4 + end5 + end6, end = '')
print(end7 + end8 + end9 + end10 + end11 + end12)

print("Hey buddy, how are you doing?", end = ' ')
print("Nice spell of weather we're having, eh?")
