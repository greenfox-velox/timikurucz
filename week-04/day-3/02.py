# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

redLine = canvas.create_line(50, 50, 100, 50, fill='red')
greenLine = canvas.create_line(50, 50, 50, 70, fill='green')
blueLine = canvas.create_line(50, 70, 100, 70, fill='blue')
blackLine = canvas.create_line(100, 70, 100, 50)

root.mainloop()
