people = 40
cars = 30
trucks = 20

# First boolean statement. Comparison statement of greater than if this is true it will print
if cars > people:
    print("We should take the cars.")
# Second statement: If the the above is false then it moves to this line.
# If this line is true it will print. If not it will go to final block.
elif cars < people:
    print("We should not take the cars.")
# This is the final block. If all above statements are false than it prints this line.
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if cars > people and trucks < cars:
    print("We might be able to figure this out.")
elif cars == people or trucks == cars:
    print("CARS CARS CARS!")
else:
    print("Screw driving!")
