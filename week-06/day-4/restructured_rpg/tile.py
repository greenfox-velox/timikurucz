from tkinter import *

class BoardElement():
    def __init__(self, x, y, canvas):
        self.size = 72
        self.x = x
        self.y = y
        self.canvas = canvas
    def draw(self, img):
        self.canvas.create_image(self.x * self.size, self.y * self.size, image = img, anchor = NW)
