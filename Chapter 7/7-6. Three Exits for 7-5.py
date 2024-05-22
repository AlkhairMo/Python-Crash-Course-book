age = ''
while age != 'quit':
    age = input('How old are you: ')
    if age != 'quit':
        age = int(age)
        if age < 3:
            print('Your ticket is free!')
        elif 3 <= age <= 12:
            print('This ticket cost 10$.')
        elif age > 12:
            print('This ticket cost 15$.')
