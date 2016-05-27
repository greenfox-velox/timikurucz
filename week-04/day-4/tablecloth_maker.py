from tkinter import*
root = Tk()

canvas_size = 1200
canvas = Canvas(root, width = canvas_size , height = canvas_size )
canvas.pack()

def make_kockas_terito(size):
    for i in range(9):
        for j in range(9):
            x_start_coord = i * size
            y_start_coord = j * size
            color = 'pink'
            if j % 2 == 0 and i % 2 == 0:
                color = 'red'
            if j % 2 != 0 and i % 2 != 0:
                color = 'white'
            canvas.create_rectangle(x_start_coord, y_start_coord, x_start_coord+size, y_start_coord+size, fill=color, width=0)
make_kockas_terito(80)

root.mainloop()
