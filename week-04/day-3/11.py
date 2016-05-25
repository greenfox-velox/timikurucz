# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
import random

from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def random_color():
    r = lambda: random.randint(0,255)
    return ('#%02X%02X%02X' % (r(),r(),r()))

def square_drawing(size, color):
    top_left = (300 - size)/2
    bottom_right = top_left + size
    square = canvas.create_rectangle(top_left, top_left, bottom_right, bottom_right, fill=color)

for size in range(201, 1, -10):
    square_drawing(size, random_color())

root.mainloop()
