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


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")
"\n"
print("Let's make your own up by doing smoothie-nomics!")

two_smalls = add(14, 14)
four_mediums = multiply(4,18)
customer_appreciation = subtract(24, 8)
tips = divide(400, 7)

print(f"Amy wants two small blueberry bananas. That is {two_smalls} ounces.")
print(f"John just ordered a bunch of chocolate smoothies!! Four to be exact! We need {four_mediums} ounces in the blender!!")
print(f"Tony didn't like his juice. Customer appreciate his order. Tell him his new total is ${customer_appreciation}.")
print(f"Everyone has their tips! Everyone got ${tips}")
