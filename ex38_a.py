animals = "Bears Lions Tigers Gorillas Chimpanzees Parrots Giraffes"

split_animals = animals.split(' ')

print("These animals are in the Zoo.")
for zoo in split_animals:
    print(f"We have: {zoo}")


aquatic_animals = ['Dolphins', 'Whales', 'Orcas', 'Tuna']
print("Wait I think we can add more aquatic friends!")

more_aquatic = ['Turtles', 'Sharks', 'Electric Eels', "Salmon"]
print("Currently we have:\n",aquatic_animals)
print("Let's also add\n", more_aquatic)
aquatic_animals.append(more_aquatic)

print("Now we have all the aquatic life together!\n", aquatic_animals)

students = ['Charlie', 'Ann', 'Bobby', 'Tony', 'Sarah', 'Kristie']

print(students[3])
print(students.pop())
print(' & '.join(students[2:5]))


employees = ['Josh', 'Mike', 'Bella', 'Raquel']

more_employees = ['Rebel', 'Laura', 'Emily', 'Scott']

print(f"Currently we have {employees} on our team!")
print("BUT!! We just hired some new team members.")

print(f"They are: {more_employees} ")
employees.append(more_employees)

print("Here is the full team!")
