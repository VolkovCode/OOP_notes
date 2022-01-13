# 18. ООП: Дескрипторы. Non-data дескрипторы

from time import time
from random import choice

class Epoch:
    def __get__(self, intance, owner_class):
        return int(time())

class MyTime:
    epoch = Epoch()

m = MyTime()

class Dice():
    @property
    def number(self):
        return choice(range(1, 7))

class Choice:
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, obj, owner):
        return choice(self._choice)

class Game:
    dice = Choice(1, 2, 3, 4, 5, 6)
    flip = Choice('Heads', 'Tails')
    r_p_s = Choice('Rock', 'Paper', 'Scissors')

#class Game:
    #@property
    #def rock_paper_scissors(self):
    #    return choice(['Rock', 'Paper', 'Scissors'])

   # @property
   # def flip(self):
   #     return choice(['Heads', 'Tails'])

  #  @property
  #  def dice(self):
   #     return choice(range(1, 7))    

g = Game() 
print(g.flip)       


        