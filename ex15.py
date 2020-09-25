# This line of code is pulling from the system the argument variable (argv)
from sys import argv

# Here we are giving the information we want in the argv
# Which we have two "script" and "filename"
script, filename = argv

# Here we are giving a variable name to the file name. BUT to be able to read it
# we have to open the file.
txt = open(filename)

# Here we are formatting the sentence to have {filename} in there to give us the name of file.
# This is basically a little message.
print(f"Here's your file {filename}:")
# Then we are asking the program to print the file, but the file has to use the funtion "read()"
# You give the file a command by using the .(dot), the name of the command,
# and parameters.
print(txt.read())
txt.close()
print("The file is now closed.")

# Little message
print("Type the filename again:")
# Using the input argument to retrieve name of file
file_again = input("> ")

# We need to open said file
txt_again = open(file_again)

# Then we need to be able to read the file.
print(txt_again.read())
txt_again.close()
