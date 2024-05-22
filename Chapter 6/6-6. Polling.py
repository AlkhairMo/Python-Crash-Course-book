favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
nopool = ['jen', 'edward']
for name in nopool:
    print(name.title())
for name in favorite_languages.keys():
    if name not in nopool:
        print(f'Thank you {name.title()} for responding!')
    else:
        print(f'Dear {name.title()}, please take the pool')
