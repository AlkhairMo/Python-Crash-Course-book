sandwich_orders = ['pastrami', 'egg', 'pastrami', 'seafood', 'chicken', 'pastrami', 'beef', 'grilled']
print('The deli has run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    print(f'{sandwich}')