name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

centimeter_height = height * 2.54
kilogram_weight = weight * 0.453

new_weight = kilogram_weight
new_height = centimeter_height

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {new_height} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {new_weight} kilograms.")
print("Actaully that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
