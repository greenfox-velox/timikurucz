from tkinter import *
from board_element import *

class Floor(BoardElement):
    def __init__(self, x, y, canvas):
        super().__init__(x,y, canvas)
        self.floor_img = PhotoImage(file = 'floor.png')

    def draw(self):
        super().draw(self.floor_img)
