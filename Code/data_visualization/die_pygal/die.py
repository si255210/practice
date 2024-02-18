from random import choice
class Die():
    def __init__(self,num_sides=6):
        self.num_sides =num_sides
    def roll(self):
        return choice(range(1,self.num_sides))   