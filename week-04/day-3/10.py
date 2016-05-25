# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.


from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_drawing(size):
    top_left = (300 - size)/2
    bottom_right = top_left + size
    square = canvas.create_rectangle(top_left, top_left, bottom_right, bottom_right)

for size in range(1, 201, 10):
    square_drawing(size)

root.mainloop()
