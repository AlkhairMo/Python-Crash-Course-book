def sandwich(*items):
    print('Your sandwich has:')
    for item in items:
        print(f'- {item.title()}')