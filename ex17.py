# Exercise 17

# Importing two packages here
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Unpacking argv into 3 variables
print(f"Copying from {from_file} to {to_file}")

# Condensed this down to one line so that we're opening and reading here
indata = open(from_file).read()


# F-string where we are throwing in the function len()
print(f"The input file is {len(indata)} bytes long")
print(f"And here is what the file says: '{indata}'")

# Using a function called exists here - not sure what it does yet
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Opening up the to_file in write mode
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
