# This is an example of a dictionary
# a dictionary is a way to map one thing to another
# this example is a dictionary with a KEY "apple"
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# This is an example of a module that has been created named mystuff
# That module is "called" by using import to bring the fuctions and variables it has
# you access the fuctions or variables with the . (dot) operator
import mystuffex
mystuffex.apple()
print(mystuffex.tangerine)

################################################################################

print(mystuff['apple']) # get apple from dict
mystuffex.apple() # get apple from module
print(mystuffex.tangerine) # same thing, it's just a variable

################################################################################

class MyStuff_class(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff_class()
thing.apple()
print(thing.tangerine)
