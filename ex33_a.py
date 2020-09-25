def less_than(high, increase):

    i = 0
    numbers = []

    while i < high:
        # print(f"At the top is {i}")
        numbers.append(i)

        i = i + increase
        print("Numbers now: ", numbers)
        # print(f"At the bottom i is {i}")



    print("The numbers: ")
    return numbers

numbers = less_than(20, 2)

for num in numbers:
    print(num)

print()
print('*'*20)
print()

def for_less_than(high, increase):
    i = 0
    numbers = []
    for num in range(i,high,increase):
        numbers.append(num)
        i = i + increase
        print("Numbers now: ", numbers)
        print(">>>i=",i)
    print("The numbers: ")
    return numbers

number_2 = for_less_than(20, 2)

for num in number_2:
    print(num)
