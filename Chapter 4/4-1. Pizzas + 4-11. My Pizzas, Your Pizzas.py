pizzas = ['peperoni', 'meat', 'chicken', 'hotdog']
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(f'I like {pizza} pizza')
print('I really like pizza!')
friend_pizzas = pizzas[:]
pizzas.append("vegetables")
friend_pizzas.append('cheese')
print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('my friend favourite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)
    