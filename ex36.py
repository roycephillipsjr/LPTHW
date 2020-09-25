from sys import exit

end_credits = open("end_credits.txt")
riddle_wizard = """
\"Hello there traveler!!
Welcome to my room!
You must be a wise-one because you have passed all my questions!!
BUUUUUTTTT!!!!!
It is now time to pass the final question!
A RIDDLE!!!

------------------------------------
------------------------------------
------------------------------------

I hope you are ready...

......................................
......................................
......................................
......................................


What has a great source of knowledge, but can never change.
It can be taken everywhere, but some places it is not allowed.
You can argue with it, but its mind is made up.
What am I?\""""

final_boss = """

\"Hello traveler!!
I have been watching you very closely...


I have watched you make it through my puzzles...


You solved the wizard's riddle...


You defeated my ax-man...


And hear you are in my final room...


...
...
...
...
...     well...


I think I will have to end you before you end MEEE!!"""

shovel_room_tools = ['shovel', 'lawn-mower', 'hoe', 'lightbulb', 'leaf blower']
cut_grass_tools = ['shovel','hoe', 'lightbulb', 'leaf blower']
leaf_blower_tools = ['shovel','hoe', 'lightbulb']

def final_room():
    print(final_boss)
    print("\n\n\nYou don't have much time!!")
    print("Quick!!")
    print("DO SOMETHING!!!!!")

    while True:
        choice = input("> ")
        if choice == "slash":
            print("That cuases damage, but it isn't enough to take them down!!")
            print("You might need to do more than that!")
            print("After you attack you dodge and you have another opportunity!")
        elif choice == "dodge":
            print("Good move!")
            print("You have saved yourself some more time, but you need to get them gone SOON!!")
        elif choice == "double slash":
            print("Your attack was super effective!")
            print("Duku has been killed!")
            print("You have beaten the game!\n\n\n")
            print(end_credits.read())
            print("Who was playing this game?")
            name = input("> ")
            print(f"\n\n\nThank you {name} for playing this game! See you next time!")
            exit(0)
        else:
            dead("Ohhh noooo! Duku hits you hard!")


def door_one_ax():
    print("How many times do you swing at the door?")

    while True:
        try:
            number = int(input("> "))

            if number <= 10:
                print("You start whacking at the door, but it isn't enough to break it down...")
            else:
                print("You aggressively attack the door and there is now an opening!")
                print("You enter the final room of 'Duku Underground'")
                print("The final boss awaits...")
                final_room()
        except ValueError:
            print("Try typing out a number!")


def final_entrance():
    print("\nThere are three doors in front of you.")
    print("Which one will you choose? '1', '2', or '3'")
    while True:
        choice = input("> ")

        if choice == "1":
            print("Do you have a way to open this door now?")

            choice = input("> ")
            if choice == "yes":
                print("What do you have then?")

                choice = input("> ")
                if choice == "an ax":
                    print("You pull out your ax and get ready to break down the door.")
                    door_one_ax()
                else:
                    print("Well that isn't going to really work now is it??")
                    print("Go back to the entrance.")
                    final_entrance()
            else:
                print("Go back to the entrance...")
                final_entrance()

        elif choice == "2":
            print("It seems as though this door is now locked and sealed...")
            final_entrance()
        elif choice == "3":
            print("It seems as though this door is now locked and sealed...")
            final_entrance()
        else:
            print("I will be nice and not kill you since you have made it this far.")
            print("Please just choose the only remaining door left!!")


def shovel_room():
    def ax_boss():
        print("\nOh no!!")
        print("The sun has immediately gone down and it is now dark.")
        print("Someone starts walking up to you.")
        print("."*50)
        print("."*50)
        print("."*50)
        print("They don't look too friendly...")
        print("."*50)
        print("."*50)
        print("."*50)
        print("\nIt looks like they have an ax and are trying to kill you!!!!")
        print("You grab your sword and prepare for battle!!")
        print("How are you going to win this battle?")

        while True:
            choice = input("> ")

            if choice == "slash":
                print("That move was quite effective and he is dead!!")
                print("He falls to the floor and drops his ax.")
                print("The ax might be useful.")
                print("Do you want to pick up the ax?")

                while True:
                    choice = input("> ")
                    if choice == "yes" or choice == "grab ax":
                        print("You now have the ax in your items.")
                        print("The door behind you opens up.")
                        print("You make it back to the entrance.")
                        print("The door behind you closes shut and is sealed.")
                        final_entrance()
                    elif choice == "pick up ax":
                        print("You now have the ax in your items.")
                        print("The door behind you opens up.")
                        print("You make it back to the entrance.")
                        print("The door behind you closes shut and is sealed.")
                        final_entrance()
                    else:
                        print("I would reccomend that you take the ax. It might be useful...")
            elif choice == "stab":
                print("You cause some damage to villan, but it isn't significant enough to kill them.")
                print("You dodge his attack and he is open for another attack.")
            else:
                print("That doesn't do anything to the villan.")
                print("You dodge his attack and he is open for another attack.")

    def leaf_blower():
        print("\nYou turn on the leaf blower and blow all the debris away.")
        print("You see there is an \"X\" in the grass now.")
        print("Maybe there is something hidden under there??")
        print("What should we use to get that item??\n")
        for leaf_tools in leaf_blower_tools:
            print("-", leaf_tools)

        while True:
            choice = input("> ")

            if choice == "shovel":
                print("Lovely choice!!")
                print("You start digging and digging...")
                print("You hit a hard box of some sort!!")
                print("\nDo you open it??")

                choice = input("> ")
                if choice == "yes":
                    print("You open the chest...")
                    print("Inside that chest is a sword!!!")
                    ax_boss()
                else:
                    print("You really get this far to not see what's inside?")
                    dead("I'm sorry to do this to you but....")
            elif choice == "hoe":
                print("Not useful here! ;)")
            elif choice == "lightbulb":
                dead("You and that lightbulb!!")
            else:
                print("Try that again my friend...")

    def cut_grass():
        print("\nThe grass is now cut,")
        print("But now there is mulch everywhere")
        print("We need to clear the way to help us see the area...")
        print("What tool should we use next?\n")
        for less_tools in cut_grass_tools:
            print("-", less_tools)

        light_bulb = False

        while True:
            choice = input("> ")

            if choice == "shovel":
                print("""This would take forever to move the mulch.
Maybe there is a more effecient way of doing this.""")
            elif choice == "hoe":
                print("Not useful here")
            elif choice == "lightbulb" and not light_bulb:
                print("""Really again with the lightbulb??
It's useless. If you choose this again you will regret it!""")
                light_bulb = True
            elif choice == "lightbulb" and light_bulb:
                    dead("I told you not to type this again!!")
            elif choice == "leaf blower":
                print("I think this might be super useful!!")
                leaf_blower()
            else:
                print("Why don't you try that again...")


    print("\nYou are now outdoors.")
    print("The room is filled with grass and what looks like some tools.")
    print("The tools you have are:\n")
    for tools in shovel_room_tools:
        print("-", tools)

    print("\nWhich tool whould you like to use?")
    while True:
        choice = input("> ")
        if choice == "shovel":
            print("Where do you want to dig? The grass is way to high to do anything.")
        elif choice == "lawn-mower":
            print("""That seems to be a wise choice.
We got to cut down this grass down to be able to see anything.""")
            cut_grass()
        elif choice == "hoe":
            print("Not usefule here")
        elif choice == "lightbulb":
            print("We are outdoors my friend. This will be of no use.")
        elif choice == "leaf blower":
            print("Maybe at some point... But this is of no use for us now...")
        else:
            print("Really a full list of items and you choose none of them?!?!")
            dead("Just due to your ingonorance I will kill you.")


def door_three_key():
    print("You have picked door 3.")
    print("It seems as though the door is locked.")
    print("Do you have a way to unlock it?")

    choice = input("> ")
    if choice == "yes":
        print("What do you have to open this door?")

        choice = input("> ")
        if choice == "wizards key":
            print("It looks like that worked!!")
            print("The door is unlocked and you walk in...")
            shovel_room()
        else:
            print("I don't think that will open it. Try again.")
            door_three_key()
    else:
        print("It seems like you don't have the right tools. Take a step back.")
        wizard_solved()

def door_one():
    print("\nYou have picked door 1.")
    print("It seems as though the door is locked.")
    print("But not only is it locked. The key-hole seems to be completely melted.")
    print("Do you have a way to get in?")

    choice = input("> ")
    if choice == "yes":
        print("What do you have to get through this door?")

        choice = input("> ")
        if choice == "an ax":
            print("You have no items on you at this moment.")
            print("Maybe you should go exploring to find something for this door.")
            entrance()
        else:
            print("I don't think that will open it. Try again.")
            door_one()
    else:
        print("It seems like you don't have the right tools. Back to the entrance.")
        entrance()


def door_three():
    print("\nYou have picked door 3.")
    print("It seems as though the door is locked.")
    print("Do you have a way to unlock it?")

    choice = input("> ")
    if choice == "yes":
        print("What do you have to open this door?")

        choice = input("> ")
        if choice == "wizards key":
            print("You have no items on you at this moment.")
            print("Maybe you should go exploring to find something for this door.")
            entrance()
        else:
            print("I don't think that will open it. Try again.")
            door_three()
    else:
        print("It seems like you don't have the right tools. Back to the entrance.")
        entrance()



#This is what happens when you die
def dead(why):
    print(why, "You have died. Try again...")
    exit(0)

def wizard_solved():
    while True:
        print("\nThere are three doors in front of you.")
        print("Which one will you choose? '1', '2', or '3'")
        choice = input("> ")
        if choice == "1":
            print("Do you have a way to open this door now?")

            choice = input("> ")
            if choice == "yes":
                print("What do you have then?")

                choice = input("> ")
                if choice == "wizards key":
                    print("That won't work here. Go back to the entrance.")
                    wizard_solved()
                else:
                    print("Well that isn't going to really work now is it??")
                    print("Go back to the entrance.")
                    wizard_solved()
            else:
                print("Go back to the entrance...")
                wizard_solved()

        elif choice == "2":
            print("It seems as though this door is now locked and sealed...")
            wizard_solved()
        elif choice == "3":
            door_three_key()
        else:
            dead("You stumble around the room until you starve.")

#This is so when you go back to the beginning you don't keep getting the welcome message
def entrance():
    print("\nBack at the entrance...")
    print("There are three doors in front of you.")
    print("Which one will you choose? '1', '2', or '3'")
    choice = input("> ")
    if choice == "1":
        door_one()
    elif choice == "2":
        door_two()
    elif choice == "3":
        door_three()
    else:
        dead("You stumble around the room until you starve.")


def key_room():
    print("\nYou have entered the Riddle Wizard's room.")
    print("The Riddle Wizard has appeared!")
    print(riddle_wizard)

    while True:
        choice = input("> ")
        if choice == "a book":
            print("\n\"You have quite the wits traveler...\"")
            print("\"As a gift for guessing correctly\"")
            print("The Riddle Wizard disappears and a key appears in his place.")
            print("\nDo you take the key?")

            choice = input("> ")
            if choice == "yes":
                print("\nYou grab the key.")
                print("You now have the 'wizards key'. You might be able to use it somewhere.")
                print("You disappear and are back at the entrance.")
                wizard_key = True
                wizard_solved()
            else:
                dead("You stubborn fool!")
        else:
            print("Try again traveler...")

def booby_trap():
    print("\nYou have entered an empty room...")
    print("Something seems too simple about this room...")
    print("There is a sign to your left do you read it?")

    def last_step():
        print("You are almost there.")
        print("\nWhat is the purpose to the universe?")

        choice = input("> ")

        if choice == "42":
            print("You are right!")
            print("Take two steps forward.")
            print("You have made it to the door.")
            print("\nDo you dare enter it?")

            choice = input("> ")
            if choice == "enter room" or choice == "yes":
                key_room()
            else:
                dead("You made it this far just to die!!")
        else:
            dead("Sorry, but that is incorrect.")


    def diagonal():
        print("\nSometimes it is wise not step forward/backward \nor step side by side")
        print("What could the next best move be?")

        while True:
            choice = input("> ")
            if choice == "step diagonally":
                print("You are a wise one.")
                print("You have made the right step ;)")
                last_step()
            elif choice == "diagonally":
                print("That is a direction to go in, but you have to do what?")
            else:
                dead("You have choosen incorrectly...")


    def forward_two():
        print("Making some progress...")
        print("\nWhat is (2 * 3) + 8 / 2 - 4?")

        choice = input("> ")

        if choice == "6":
            print("Now take two steps to the left and one forward.")
            diagonal()
        else:
            dead("Time to refresh those math skills!")

    def forward():
        print("\nYou have made your first right move.")
        print("Now for your first puzzle...")
        print("What is the capital of Montana?")
        choice = input("> ")

        if choice == "Helena":
            print("Correct!! You now take 2 steps forward...")
            forward_two()
        else:
            dead("Look at a map buddy!!")

    while True:
        choice = input("> ")

        if choice == "yes" or choice == "read":
            print("\tThis is the \"Booby Trap\" room.")
            print("\tYou have to be very careful in here.")
            print("\tBecause one wrong step could be dangerous.")
            print("""\tAnswer your questions wisely as they will give
        you clues to make it through.""")
            print("\tGo ahead 'step forward' to get started...")

            while True:
                choice = input("> ")

                if choice == "step forward":
                    forward()
                else:
                    print("Come on the answer was given to you!!")

        else:
            print("Good luck...")
            choice = input("> ")
            if choice == "step forward":
                forward()
            else:
                dead("Maybe you should have read the sign.")


def door_two():
    print("\nYou have choosen the second door.")
    print("The door seems to be unlocked.")
    print("Do you enter the room?")

    while True:
        choice = input("> ")

        if choice == "enter room" or choice == "yes":
            booby_trap()
        elif choice == "start":
            entrance()
        else:
            print("What else are you going to do??")


def start():
    print("Welcome to 'Duku's Underground'")
    print("You have just entered the lair.")
    print("""You will encounter many things in here.
Hopefully you are able to figure out the puzzles.
If not you will experience a painful death.
Good luck!""")
    print("\nThere are three doors in front of you.")
    print("Which one will you choose? '1', '2', or '3'")

    choice = input("> ")
    if choice == "1":
        door_one()
    elif choice == "2":
        door_two()
    elif choice == "3":
        door_three()
    else:
        dead("You stumble around the room until you starve.")


start()
