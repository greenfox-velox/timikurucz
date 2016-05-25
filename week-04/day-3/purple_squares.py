# from tkinter import*
# root = Tk()
#
# canvas = Canvas(root, width='300', height='300')
# canvas.pack()
#
# def square_drawing(size):
#     top_left = 10
#     bottom_right = top_left + size
#     for i in range(20):
#         position = size*i
#         square = canvas.create_rectangle(top_left+position, top_left+position, bottom_right+position, bottom_right+position, fill='purple')
# square_drawing(10)
# root.mainloop()

from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_drawing(x, y, size):
    for i in range(20):
        square = canvas.create_rectangle(x*i, y*i, x+(size*i), y+(size*i), fill='purple')

square_drawing(10, 10, 10)
root.mainloop()



# from tkinter import*
# root = Tk()
# canvas = Canvas(root, width='300', height='300')
# canvas.pack()
#
# def square_drawing(position):
#     size = 10
#     for i in range(1, 20):
#         square = canvas.create_rectangle(position*i, position*i, position+size*i, position+size*i, fill='purple')
#
# square_drawing(10)
# root.mainloop()
