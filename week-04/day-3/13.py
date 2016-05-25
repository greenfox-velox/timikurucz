# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import*
root = Tk()

width = 300
height = 300
canvas = Canvas(root, width=width, height=height)
canvas.pack()

center_x = width // 2
center_y = height // 2

def line_drawing(x, y):
    line = canvas.create_line(x, y, center_x, center_y, fill='green')

for i in range(16):
    x = i * 20
    y = i * 20
    line_drawing(x, 0)
    line_drawing(x, height)
    line_drawing(0, y)
    line_drawing(width, y)

line_drawing(0, 0)
root.mainloop()
