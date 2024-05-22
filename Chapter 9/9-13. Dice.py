from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        print(result)


dice = Dice()
print('6-sided die results:')
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice = Dice(10)
print('10-sided die results:')
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice = Dice(20)
print('20-sided die results:')
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
