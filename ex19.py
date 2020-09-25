# Here we are starting to define our varible. Which is cheese_and_crackers.
# Then we make the arguments of what we want our varible to have which is:
# cheese_count and boxes_of_crackers.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# We then have our indented line of code to tell what the funtion does.
# We want our funtion to print out how much cheese and crackers we have
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
# \n to creat a new line to make space in between our four different arguments
    print("Get a blanket.\n")

# Starting with a simple giving of the function directly to variable_name which is cheese_and_crackers
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Here creating variables to put into the function. Then adding those variables to the variable_name
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Doing math inside the variable_name
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Doing math and using the variables from line 19 to get a new total.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
