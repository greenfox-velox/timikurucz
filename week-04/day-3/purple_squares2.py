from tkinter import*
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_drawing(x, y, size):
    for i in range(6):
        square = canvas.create_rectangle(x, y, x+size, y+size, fill='purple')
        x += size
        y += size
        size +=10

square_drawing(10,10,10)

# square = canvas.create_rectangle(10, 10, 20, 20, fill='purple')
# --> a vegkoordinatak nonek 10-zel
# square = canvas.create_rectangle(20, 20, 40, 40, fill='purple')
# --> a vegkoordinatak nonek 20-szal
# square = canvas.create_rectangle(40, 40, 70, 70, fill='purple')
#--> a vegkoordinatak nonek 30-cal
# square = canvas.create_rectangle(70, 70, 110, 110, fill='purple')

#a vegkoordinataknonek a merettel
#a meret pedig mindig no 10-zel

root.mainloop()
