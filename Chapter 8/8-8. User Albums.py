def make_album(artist, title):
    album = {'artist name': artist, 'album title': title}
    return album


while True:
    print('Enter the album information')
    print('Anytime you want to quit just type "q"')
    name = input('Artist name: ')
    if name == 'q':
        break
    header = input('Album title: ')
    if header == 'q':
        break
    new_album = make_album(name, header)
    print(new_album)
