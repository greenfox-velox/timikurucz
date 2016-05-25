# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

green_square = canvas.create_rectangle(0, 0, 40, 300, fill='green')
yellow_square = canvas.create_rectangle(40, 100, 240, 300, fill='yellow')
red_square = canvas.create_rectangle(240, 100, 300, 300, fill='red')
blue_square = canvas.create_rectangle(40, 0, 300, 100, fill='blue')

root.mainloop()
