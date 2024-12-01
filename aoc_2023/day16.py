class TheFloorWillBeLava:
    def __init__(self, content):
        self.contraption = content
        for row in self.contraption:
            print(row)
        rows, columns = len(self.contraption), len(self.contraption[0])
        self.grid = [[0 for _ in range(rows)] for _ in range(columns)]
        self.run_light(row=0, column=0, dir_row=0, dir_column=1)

    def run_light(self, row, column, dir_row, dir_column):
        run = True
        while run and row >= 0 and row < len(self.contraption) and column >= 0 and column < len(self.contraption[0]):
            cell = self.contraption[row][column]
            print(row, column, cell)
            self.grid[row][column] = 1
            if dir_column == 1:
                if cell == "/":
                    print("dtected / from left")
                    dir_column = 0
                    dir_row = -1
                if cell == "\\":
                    print("dtected \\ from left")
                    dir_column = 0
                    dir_row = 1
                if cell == "|":
                    run = False
                    print("dtected | from left")
                    self.run_light(row=row+1, column=column, dir_row=1, dir_column=0)
                    self.run_light(row=row-1, column=column, dir_row=-1, dir_column=0)
            
            elif dir_column == -1:
                if cell == "/":
                    print("dtected / from right")
                    dir_column = 0
                    dir_row = 1
                if cell == "\\":
                    print("dtected \\ from right")
                    dir_column = 0
                    dir_row = -1
                if cell == "|":
                    print("dtected | from right")
                    run = False
                    self.run_light(row=row+1, column=column, dir_row=1, dir_column=0)
                    self.run_light(row=row-1, column=column, dir_row=-1, dir_column=0)

            elif dir_row == 1:
                if cell == "/":
                    print("dtected / from up")
                    dir_column = -1
                    dir_row = 0
                if cell == "\\":
                    print("dtected \\ from up")
                    dir_column = 1
                    dir_row = 0
                if cell == "-":
                    print("dtected - from up")
                    run = False
                    self.run_light(row=row, column=column+1, dir_row=0, dir_column=1)
                    self.run_light(row=row, column=column-1, dir_row=0, dir_column=-1)
            
            elif dir_row == -1:
                if cell == "/":
                    print("dtected / from down")
                    dir_column = 1
                    dir_row = 0
                if cell == "\\":
                    print("dtected \\ from down")
                    dir_column = -1
                    dir_row = 0
                if cell == "-":
                    print("dtected - from down")
                    run = False
                    self.run_light(row=row, column=column+1, dir_row=0, dir_column=1)
                    self.run_light(row=row, column=column-1, dir_row=0, dir_column=-1)

            row = row + dir_row
            column = column + dir_column

    def energized_cells(self):
        cells = 0
        for y in self.grid:
            print(y)
            for x in y:
                cells = cells + x
        print(cells)
    