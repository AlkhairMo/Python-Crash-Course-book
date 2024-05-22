glossary = {'print()': 'print the variable as output',
            '.upper()': 'string method change it to uppercase',
            '.lower()': 'string method change it to lowercase',
            '.strip()': 'string method remove spaces right or left it',
            '.insert()': 'list method add an element in a specific place in it',
            '.append()': 'list method add an element in the last of it',
            '.pop()': 'list method remove an item by its index and let you use it again',
            'del': 'statement remove an item by its index and you can not use it again',
            '.remove()': 'list method remove an item by its value',
            '.sort()': 'list method sort it paramently in alphabetical order',
            'sorted()': 'function sort alphabetical for a time',
            '.reverse()': 'list function revers its order'
            }
for term, meaning in glossary.items():
    print(f'{term}:\n{meaning}\n')
