i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")



print("The numbers: ")

for num in numbers:
    print(num)

for i in range(0, 9):
    print(f"I am trying a for loop: {i}")
