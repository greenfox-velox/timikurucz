from board_element import *
from floor import *
from wall import *
from area import *

class Map():
    def __init__(self, canvas, input_map):
        self.map_output = []
        self.input_map = input_map
        self.canvas = canvas

    def create_map(self):
        self.output = []
        for x in range(len(self.input_map)):
            for y in range(len(self.input_map[x])):
                if self.input_map[y][x] == 0:
                    self.output.append(Floor(x, y, self.canvas))
                else:
                    self.output.append(Wall(x, y, self.canvas))
        return self.output

    def create_board(self):
        for i in self.output:
            i.draw()

    def is_in_boundaries(self, x, y):
        return y <= 9 and y >= 0 and x >= 0 and x <= 9

    def next_is_floor(self, x, y):
        return map_tile[y][x] == 0

    def next_floor_is_occupied(self, x, y, enemy):
        return x == enemy.x and y == enemy.y
