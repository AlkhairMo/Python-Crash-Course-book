import time

sandwich_orders = ['egg', 'seafood', 'chicken', 'beef', 'grilled']
finished_sandwiches = []
while sandwich_orders:
    finished = sandwich_orders.pop()
    print(f'I made your {finished} sandwich')
    time.sleep(1)
    finished_sandwiches.append(finished)
print('finished sandwiches: ')
for sandwich in finished_sandwiches:
    print(f'{sandwich}')
