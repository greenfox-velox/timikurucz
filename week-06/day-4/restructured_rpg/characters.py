from tkinter import *
from board_element import *
from random import randint
from gameboard import *


class Character(BoardElement):
    def __init__(self, x, y, canvas):
        super().__init__(x, y, canvas)
        self.rolled_num = self.roll_dice()
        self.current_hp = 0
        self.level = 1

    def roll_dice(self):
        rolled_num = randint(1, 6)
        return rolled_num

    def is_alive(self):
        return self.current_hp > 0
