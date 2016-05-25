from tkinter import*
root = Tk()
canvas_size = 320
canvas = Canvas(root, width=canvas_size, height=canvas_size, bg='white')
canvas.pack()

size = canvas_size // 8

def square_drawing(x, y):
    for z in range(8):
        x = 0
        if z % 2 !=0:
            for i in range(8):
                if i % 2 != 0:
                    square = canvas.create_rectangle(x, y, x+size, y+size, fill='purple')
                x += size
        else:
            for i in range(8):
                if i % 2 == 0:
                    square = canvas.create_rectangle(x, y, x+size, y+size, fill='purple')
                x += size
        y +=size

square_drawing(0, 0)


# square = canvas.create_rectangle(0, 0, 40, 40, fill='purple')
# square = canvas.create_rectangle(40, 0, 80, 40, fill='green')
# square = canvas.create_rectangle(80, 0, 120, 40, fill='purple')
# square = canvas.create_rectangle(120, 0, 160, 40, fill='green')
# square = canvas.create_rectangle(160, 0, 200, 40, fill='purple')
# square = canvas.create_rectangle(200, 0, 240, 40, fill='green')

root.mainloop()
