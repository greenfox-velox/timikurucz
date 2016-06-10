from tkinter import *
from board_element import *
from random import randint
from gameboard import *

class Boss(Character):
    def __init__(self, canvas, map_tile, x, y):
        super().__init__(x, y, canvas)
        self.boss_img = PhotoImage(file = 'boss.png')
        self.name = 'Boss'
        self.map_tile = map_tile
        self.level = 1
        self.max_hp = 0
        self.current_hp = 2 * self.level * self.rolled_num + self.rolled_num
        self.defend_point = (self.level / 2) * self.rolled_num + (self.rolled_num / 2)
        self.strike_point = self.level * self.rolled_num + self.level
        self.strike_value = self.strike_point

    def draw(self):
        super().draw(self.boss_img)
