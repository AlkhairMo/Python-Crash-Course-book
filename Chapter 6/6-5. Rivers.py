rivers = {'nile': 'sudan',
          'amazon': 'brazil',
          'digla': 'iraq',
          }
for river, country in rivers.items():
    print(f'{river.title()} river is run through {country.title()}.')
print('\n')
for river in rivers.keys():
    print(river)
print('\n')
for country in rivers.values():
    print(country)
