topping = ''
while topping != 'quit':
    topping = input('Enter what do you want on your pizza'
                    '\nEnter quit when you finish: ')
    if topping != 'quit':
        print(f'{topping.title()} added to you pizza.\n')
