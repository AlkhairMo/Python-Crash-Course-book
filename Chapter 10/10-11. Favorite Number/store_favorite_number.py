import json

favorite_number = input('What is your favorite number? ')
with open('favorite_number.json', 'w') as f:
    json.dump(favorite_number, f)

