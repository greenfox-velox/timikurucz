from tkinter import*
master = Tk()

canvas = Canvas(master, width='300', height='300')
canvas.pack()

def draw_triangle(x, y, size):
    height = (size**2 - (size/2)**2)**0.5
    canvas.create_polygon(x, y, x+size, y, x+size/2, y+height, fill='white', outline='black')

def fractal(x, y, size):
    draw_triangle(x, y, size)
    if size < 5:
        pass
    else:
        small_height = ((size**2 - (size/2)**2)**0.5)/2
        fractal(x, y, size/2)
        fractal(x+size/2, y, size/2)
        fractal(x+size/4, y+small_height, size/2)

fractal(0,0,300)

master.mainloop()
