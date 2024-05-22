def make_album(artist, title, songs=None):
    album = {'artist name': artist, 'album title': title}
    if songs:
        album['number of songs'] = songs

    return album


new_album = make_album('the weeknd', 'after hours', songs=14)
print(new_album)
new_album = make_album(title='happier than ever', artist='billie eilish')
print(new_album)
new_album = make_album(title='no doubt', artist='tragic kingdom')
print(new_album)
new_album = make_album('travis scott', 'astroworld', 17)
print(new_album)
