# There are 10 people and we are giving it a name of types_of_people(variable_name_)
types_of_people = 10
# Here we are giving the variable x a value of f"There are {types_of_people}...}
# We are also putting the string types_of_people inside this string
x = f"There are {types_of_people} types of people."

# Giving a value to "binary"
binary = "binary"
# Giving a value to don't
do_not = "don't"
# Giving a value to y that has both previous value_names. There are 2 strings inside this one
y = f"Those who know {binary} and those who {do_not}."

# We are printing values x and y
print(x)
print(y)

# Again we are printing values x and y, but now putting them inside a string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Giving the name hilarious a boolean value of False.
hilarious = False

# Giving the variable_name "joke_evaluation" the value "Isn't that joke..."
joke_evaluation = "Isn't that joke so funny?! {}"

# Here is another example of a different way to format.
# Instead of putting "f" in front of the phrase to format that phrase you are
# intead formatting it separately.
# SO! joke_evaluation has the phrase "Isn't that joke so funny?! {}"
# Here we are choosing to print joke_evaluation, but we want to format the {}
# inside of the string. Which we are choosing the variable hilarious
print(joke_evaluation.format(hilarious))

# Giving variable_names to w and e
w = "This is the left side of..."
e = "a string with a right side."

# When adding two strings together it just puts them side by side
print(w + e)
