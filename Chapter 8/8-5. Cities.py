def describe_city(name, country='United State'):
    print(f'{name.title()} is in {country.title()}')


describe_city('new york')
describe_city(name='los angelos')
describe_city('reykjavik', 'iceland')

