# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.


from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def line_drawing(x, y):
    line = canvas.create_line(x, y, x+50, y)
    return line

line_drawing(20, 20)
line_drawing(50, 30)
line_drawing(100, 160)

root.mainloop()
