# create a 300x300 canvas.
# draw its diagonals in green.

from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
start = 0
end = 300
line = canvas.create_line(start, start, end, end)

root.mainloop()
