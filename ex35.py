from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    try:
        how_much = int(input("> "))

        if how_much <= 50:
            print("Nice, you're not greedy, you win!")
            exit(0)

        else:
            dead("Buddy, you are a greedy.")
    except ValueError:
        dead("Learn to type a number!")



def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")

        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            dead_bear()

        else:
            print("I got no idea what that means.")


bear_moved = True
def dead_bear():
    while True:
        choice = input("> ")
        if choice == "taunt bear" and bear_moved:
            dead("The bear gets angry and chews your leg off.")

        elif choice == "open door" and bear_moved:
            gold_room()

        else:
            print("Try again...")



def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    cthulhu_life = False

    while True:
        choice = input("> ")

        if choice == "flee":
            start()

        elif choice == "head":
            dead("Well that was tasty!")

        elif choice == "stab":
            print("The great evil Cthulhu has turned to smoke.")
            print("There is now a key and a door.")
            cthulhu_life = True

        elif choice == "use key" and cthulhu_life:
            silver_room()

        else:
            print("""TRY AGAIN BUDDY!!
        --------------------------""")


def silver_room():
    print("You have survived the great evil Cthulhu.")
    print("You are now in the silver room.")
    print("There is a treasure chest.")

    while True:
        choice = input("> ")
        if choice == "open treasure":
            dead("You greedy greedy player!")

        elif choice == "look around":
            print("Curious for more??")
            print("Ok, that's good because the treasure was jinxed.")
            print("You win the game!")
            exit(0)

        else:
            print("I'm not sure I understand. Try again.")

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()

    elif choice == "right":
        cthulhu_room()

    else:
        dead("You stumble around the room until you starve.")


start()
