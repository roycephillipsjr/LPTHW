print("How many times do you swing at the door?")
while True:
    try:
        number = int(input("> "))

        if number <= 10:
            print("You start whacking at the door, but it isn't enough to break it down...")
        else:
            print("You aggressively attack the door and there is now an opening!")
    except ValueError:
            print("Try typing out a number!")
