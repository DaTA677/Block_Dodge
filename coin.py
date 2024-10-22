from block import Block
from config import *
from random import randrange

class Coin(Block):
    def __init__(self, x, y, width, height, velocity, colour=...):
        super().__init__(x, y, width, height, velocity, colour)
        self._value=10

    def wrap_object(self):
        if(self._y>WIN_HEIGHT+1):
           self.reset((WIN_WIDTH//self._width+15)* randrange(0,WIN_WIDTH//self._width+15), 0)

    def reset(self, x, y):
        super().reset(x, y)
        self.velocity=COIN_SPEED
    