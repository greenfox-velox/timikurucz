from tkinter import *
from board_element import *
from random import randint
from gameboard import *

class Skeleton(Character):
    def __init__(self, canvas, map_tile, x, y):
        super().__init__(x, y, canvas)
        self.hero_img = PhotoImage(file = 'skeleton.png')
        self.map_tile = map_tile
        self.level = 1
        self.HP = 2 * self.level * self.rolled_num
        self.DP = (self.level / 2) * self.rolled_num
        self.SP = self.level * self.rolled_num

    def draw(self):
        super().draw(self.hero_img)
