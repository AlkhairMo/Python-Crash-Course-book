cities = {
    'paris': {
        'country': 'france',
        'population': '2.1m',
        'fact': 'It called "City of Light"',
     },
    'london': {
        'country': 'england',
        'population': '8.9m',
        'fact': 'It is the smallest city in UK',
    },
    'new york':
    {
        'country': 'united states',
        'population': '8.4m',
        'fact': 'It was the first capital in US',
    },
}
for city, info in cities.items():
    print(f'{city.title()}:')
    print(f"\tIt is a city in {info['country'].title()}.")
    print(f"\tIt has {info['population']} population.")
    print(f"\t{info['fact']}.")
