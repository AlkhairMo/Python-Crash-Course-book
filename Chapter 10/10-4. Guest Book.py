choice = input('What do you want?(answer by numbers)\n'
               '1. Add new gust\n'
               "2. Check guest's list ")
if choice == '1':
    while True:
        guest_name = input('write quit to exit the programme\n'
                           'Enter your name: ')
        if guest_name != 'quit':
            print(f'Welcome {guest_name}')
            with open('text_files/guest_book.txt', 'a') as gust:
                gust.write(guest_name + '\n')
        else:
            break
elif choice == '2':
    with open('text_files/guest_book.txt', 'r') as gust:
        gusts = gust.readlines()
    for one_gust in gusts:
        print(one_gust.rstrip())
else:
    print('Please answer by 1 or 2')
