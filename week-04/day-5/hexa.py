from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


def draw_hexa(x, y, size):
    triangle_height=3**0.5/2*size
    canvas.create_polygon(x, y+triangle_height, x+size/2, y, x+size+size/2, y, x+2*size, y+triangle_height, x+size+size/2, y+ 2*triangle_height, x+size/2, y+2*triangle_height, fill='white', outline='black')

def fractal(x, y, size):
    draw_hexa(x, y, size)
    if size < 5:
        pass
    else:
        new_size = size/3
        total_height=(3**0.5/2*(new_size))*4

        fractal(x+new_size, y, new_size)
        fractal(x+size, y, new_size)
        fractal(x+new_size, y+total_height, new_size)
        fractal(x+3*new_size, y+total_height, new_size)
        fractal(x, y+total_height/2, new_size)
        fractal(x+4*new_size, y+total_height/2, new_size)


fractal(0,0,100)

root.mainloop()
