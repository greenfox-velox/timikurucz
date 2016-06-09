from tkinter import *
from gameboard import *


def main():
    root = Tk()
    canvas = Canvas(root, width = 1000, height = 720)
    canvas.pack()

    level1 = Board(canvas, map_tile)

    root.bind('<KeyPress>', level1.key_pressed)

    root.mainloop()

main()
