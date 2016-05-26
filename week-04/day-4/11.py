from tkinter import*
root = Tk()
canvas_size = 600
canvas = Canvas(root, width = canvas_size, height = canvas_size, bg='yellow')
canvas.pack()


def fractal(x, y, size):
    canvas.create_rectangle(x+size, y, x+2*size, y+size)
    canvas.create_rectangle(x+2*size, y+size, x+3*size, y+2*size)
    canvas.create_rectangle(x, y+size, x+size, y+2*size)
    canvas.create_rectangle(x+size, y+2*size, x+2*size, y+3*size)
    if size < 5:
        pass
    else:
        fractal(x+size, y, size/3)
        fractal(x, y+size, size/3)
        fractal(x+size*2, y+size, size/3)
        fractal(x+size, y+2*size, size/3)

fractal(0,0,200)

root.mainloop()
