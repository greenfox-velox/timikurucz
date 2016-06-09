from tkinter import *
from tile import *

class Wall(BoardElement):
    def __init__(self, x, y, canvas):
        super().__init__(x,y,canvas)
        self.wall_img = PhotoImage(file = 'wall.png')

    def draw(self):
        super().draw(self.wall_img)
