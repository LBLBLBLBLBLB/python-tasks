import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):

        for i in range(10):
            result = random.randint(1, self.sides)
            print(f"the die rolled a {result}")


die1 = Die(6)
die1.roll_dice()
print()
die2 = Die(10)
die2.roll_dice()
print()
die2 = Die(20)
die2.roll_dice()
