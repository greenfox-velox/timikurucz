from board_element import *
from characters import *
from hero import *
from skeleton import *
from boss import *
from playfield import *
from stats import *


class Board():
    def __init__(self, canvas, input_map):
        self.input_map = input_map
        self.playfield = Map(canvas, input_map)
        self.canvas = canvas
        self.bela = Hero(canvas, map_tile)
        self.boss = Boss(canvas, map_tile, 9, 3)
        self.skeletons = [Skeleton(canvas, map_tile, 4, 0), Skeleton(canvas, map_tile, 2, 6), Skeleton(canvas, map_tile, 9, 9)]
        self.stat = Stats()
        self.playfield.create_map()
        self.stat.draw_stat(canvas, self.bela, 850, 100)
        self.draw()
        # self.stat.draw_hero_stat(self.canvas)

    def key_pressed(self, event):
        next_x = self.bela.x
        next_y = self.bela.y
        if event.keysym == 'Down':
            next_y += 1
        elif event.keysym == 'Up':
            next_y -= 1
        elif event.keysym == 'Right':
            next_x += 1
        elif event.keysym == 'Left':
            next_x -= 1
        if self.playfield.is_in_boundaries(next_x, next_y) and self.playfield.next_is_floor(next_x, next_y):
            if self.playfield.next_floor_is_occupied(next_x, next_y, self.boss):
                self.stat.draw_stat(self.canvas, self.boss, 850, 500)
            self.bela.move(next_x, next_y, self.bela.images[event.keysym])
            self.draw()


    def draw_skeletons(self):
        for skeleton in self.skeletons:
            skeleton.draw()

    def draw(self):
        self.playfield.create_board()
        self.draw_skeletons()
        self.boss.draw()
        self.bela.draw()
