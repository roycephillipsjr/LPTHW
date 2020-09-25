from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# This is just a simple input waiting for you to answer
input("?")
# printing text
print("Opening the file...")
# We are opening the file here. Got to find out why 'w' is used
# target is now the file
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# This is deleting the file.
target.truncate()

print("Now I'm going to ask you for three lines.")

# asking for three inputs
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Pythong will automatically write the new lines into the file.
# "\n" is used to create a new line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# The file is closed and saved. 
target.close()
