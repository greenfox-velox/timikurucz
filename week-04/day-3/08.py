# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_drawing(x, y):
    start = x, y
    square = canvas.create_rectangle(start, x+50, y+50)
    return square

square_drawing(10, 40)
square_drawing(80, 80)
square_drawing(170, 100)

root.mainloop()
