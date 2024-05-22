people_number = input('How many people in your dinner group? ')
people_number = int(people_number)
if people_number > 8:
    print('\nYou have to wait for a table.')
else:
    print('\nYour table is ready.')