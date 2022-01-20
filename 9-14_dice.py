from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        return x


# six_sided = Die()
# i = 1
# while i < 11:
#     randnum = six_sided.roll_die()
#     print('No.' + str(i) + ': ' + str(randnum))
#     i += 1

ten_sided = Die(sides=10)
i = 1
while i < 11:
    randnum = ten_sided.roll_die()
    print('No.' + str(i) + ': ' + str(randnum))
    i += 1
