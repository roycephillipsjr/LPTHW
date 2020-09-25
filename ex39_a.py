
great_state = {'Dallas': 'TX',
               'Austin': 'TX',
               'Houston': 'TX',}

print('-' * 10)
for city, state in list(great_state.items()):
    print(f"The great state of Texas has beautiful {city} in it's state!")

print('-' * 10)
print("There are more beautiful cities to add!!")

more_texas = {'San Antonio': 'TX',
              'Fort Worth': 'TX',
              'El Paso': 'TX'}
for city, state in list(more_texas.items()):
    print(f"Let's add {city} to the list!!")

great_state['San Antonio'] = 'TX'
great_state['Fort Worth'] = 'TX'
great_state['El Paso'] = 'TX'

print('-' * 10)
print("Now the great state of Texas has: ")
for city, state in list(great_state.items()):
    print(city)

print('-' * 10)

capitols = {'Austin': 'TX',
            'Lansing': 'MI',
            'Oklahoma City': "OK",
            'Boston': 'MA',
            'Philadelphia': 'PA'}

for city, state in list(capitols.items()):
    print(f"In the state of {state} the capitol is {city}.")
