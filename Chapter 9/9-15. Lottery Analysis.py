from random import choice

winners = []
while True:
    lottery = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'c', 'i', 'm', 's')
    first = choice(lottery)
    second = choice(lottery)
    third = choice(lottery)
    fourth = choice(lottery)
    winner = [first, second, third, fourth]
    winners.append(winner)
    my_ticket = ['c', 6, 3, 'm']
    if my_ticket == winner:
        break
print(len(winners))
