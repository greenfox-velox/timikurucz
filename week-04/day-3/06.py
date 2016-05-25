# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
top_left = 145
bottom_right = 155

green_square = canvas.create_rectangle(top_left, top_left, bottom_right, bottom_right, fill='green')
canvas.pack()

root.mainloop()
