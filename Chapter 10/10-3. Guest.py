guest_name = input('Enter your name: ')
with open('text_files/guest.txt', 'w') as gust:
    gust.write(guest_name)

