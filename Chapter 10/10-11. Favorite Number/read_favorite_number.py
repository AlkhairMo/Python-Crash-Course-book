import json

with open('favorite_number.json') as f:
    favorite_number = json.load(f)

print(f"I know your favorite number! It’s {favorite_number}")
