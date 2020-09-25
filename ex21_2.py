def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?\n")

print("This is me trying to spread out into a normal function. 'I think this is the normal one.'")

what1 = divide(age, 2)
what2 = multiply( iq, what1)
what3 = subtract(height, what2)
what4 = add(weight, what3)

print(f"The total should show up here -> {what4}")

print(24 + 34 / 100 - 1023)

pants = 24
jacket = 34
shoes = 100
socks = 1023

clothes = subtract(add(pants, divide(jacket, shoes)), socks)

print(f"My clothes are gone. There are {clothes} left.")
