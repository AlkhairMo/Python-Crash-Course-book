favorite_number = {'ahmed': [100, 5],
                   'ebrahim': [8, 2, 7],
                   'alkhair': [365],
                   'mohamed': [6, 8],
                   'ali': [5, 10],
                   }
for name, numbers in favorite_number.items():
    if len(numbers) > 1:
        print(f"{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(f"{number}")
    else:
        print(f"{name.title()}'s favorite number is:")
        for number in numbers:
            print(f"{number}")
