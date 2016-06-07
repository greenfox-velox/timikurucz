from tkinter import *
root = Tk()
canvas = Canvas(root, width = 800, height = 800)
canvas_size = 800
canvas.pack()

class Tile():
    def __init__(self, x, y):
        self.size = 72
        self.x = x
        self.y = y
    def draw(self, img):
        canvas.create_image(self.y * self.size, self.x * self.size, image = img, anchor = NW)

class Floor(Tile):
    def __init__(self, x, y):
        self.floor_img = PhotoImage(file = 'floor.png')
        super().__init__(x,y)

    def draw(self):
        super().draw(self.floor_img)

class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.wall_img = PhotoImage(file = 'wall.png')

    def draw(self):
        super().draw(self.wall_img)

class Board():
    def __init__(self, input_map):
        self.input_map = input_map
        
    def create_map(self):
        self.output = []
        for i in range(len(self.input_map)):
            for j in range(len(self.input_map[i])):
                if map_tile[i][j] == 0:
                    self.output.append(Floor(i, j))
                else:
                    self.output.append(Wall(i, j))

    def create_board(self):
        for i in self.output:
            i.draw()


map_tile = ([0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0])

level1 = Board(map_tile)
level1.create_map()
level1.create_board()


root.mainloop()
