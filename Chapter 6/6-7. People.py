person_1 = {
    'first name': 'ahmed',
    'last name': 'mohamed',
    'age': '19',
    'city': 'khartoum',
            }
person_2 = {
    'first name': 'alkhair',
    'last name': 'mohamed',
    'age': '19',
    'city': 'khartoum'
        }
person_3 = {
    'first name': 'mohamed',
    'last name': 'ali',
    'age': '30',
    'city': 'khartoum',
          }
people = [person_1, person_2, person_3]
for person in people:
    print(person)
    for inf, ans in person.items():
        print(f'{inf}: {ans.title()}')
