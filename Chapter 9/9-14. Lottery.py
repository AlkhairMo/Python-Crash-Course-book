from random import choice

lottery = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'c', 'i', 'm', 's')
first = choice(lottery)
second = choice(lottery)
third = choice(lottery)
fourth = choice(lottery)
print('Any ticket matching these four numbers or letters wins a prize:\n'
      f'{first}{second}{third}{fourth}')

