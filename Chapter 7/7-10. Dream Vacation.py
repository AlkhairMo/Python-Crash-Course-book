dream_vacation = {}
while True:
    name = input('What is your name? ')
    place = input('If you could visit one place in the world, where would you go? ')
    dream_vacation[name] = place
    cont = input('Would you want to let another person respond? (yes/no) ')
    if cont == 'no':
        break
for name,place in dream_vacation.items():
    print(f'{name.title()} wish to visit {place.title()}')
