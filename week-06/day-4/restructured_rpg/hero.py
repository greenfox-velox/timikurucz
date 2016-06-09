from tkinter import *
from tile import *
from random import randint
from area import *
from gameboard import *
from characters import *


class Hero(Character):
    def __init__(self, canvas, map_tile):
        super().__init__(0, 0, canvas)
        self.hero_img = PhotoImage(file = 'hero-down.png')
        self.map_tile = map_tile
        self.max_hp = 0
        self.current_hp = 20 + (self.rolled_num + self.rolled_num + self.rolled_num)
        self.defend_point = self.rolled_num + self.rolled_num
        self.strike_point = 5 + self.rolled_num
        self.strike_value = self.strike_point
        self.level = 1
        self.stat = 'Hero (Level ' + str(self.level) + ') HP: ' + str(self.current_hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.defend_point) + ' | SP: ' + str(self.strike_point)
        self.images = {'Down' : PhotoImage(file = 'hero-down.png'), 'Up' : PhotoImage(file = 'hero-up.png'), 'Left' : PhotoImage(file = 'hero-left.png'), 'Right' : PhotoImage(file = 'hero-right.png')}

    def stat_print(self, canvas):
        return canvas.create_text(740, 360, text = self.stat, anchor = NW)

    def draw(self):
        super().draw(self.hero_img)

    def move(self, x, y, img):
        self.hero_img = img
        self.x = x
        self.y = y
