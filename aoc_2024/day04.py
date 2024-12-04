class CeresSearch:
    def __init__(self, content):
        self.array = []
        for line in content:
            array_line = []
            for char in line:
                array_line.append(char)
            self.array.append(array_line)
        
        self.rows = len(self.array)
        self.columns = len(self.array[0])
        self.directions = [
            (0, 1),   # left
            (0, -1),  # right
            (1, 0),   # up
            (-1, 0),  # down
            (1, 1),   # diagonal down right
            (-1, -1), # diagonal up lewft
            (1, -1),  # diagonal down left
            (-1, 1)   # diagonal up right
        ]
        self.search_string = "XMAS"
        self.X_serach = ['M', 'A', 'S']

    def check_directions(self, x, y, dx, dy):
        for i in range(len(self.search_string)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= self.rows or ny < 0 or ny >= self.columns or self.array[nx][ny] != self.search_string[i]:
                return False
        return True
    
    def part_one(self):
        result = 0
        for x in range(self.rows):
            for y in range(self.columns):
                for dx, dy in self.directions:
                    if self.check_directions(x, y, dx, dy):
                        result += 1
        print(result)

    def check_X(self, x, y):
        if x - 1 < 0 or x + 1 >= self.rows or y - 1 < 0 or y + 1 >= self.columns:
            return False
        
        X_pattern = [
            [self.array[x - 1][y - 1], self.array[x][y], self.array[x + 1][y + 1]],
            [self.array[x - 1][y + 1], self.array[x][y], self.array[x + 1][y - 1]]
        ]

        if X_pattern[0] == self.X_serach and X_pattern[1] == self.X_serach:
            X1 = True
        else:
            X1 = False
        if X_pattern[0] == self.X_serach[::-1] and X_pattern[1] == self.X_serach[::-1]:
            X2 = True
        else:
            X2 = False
        if X_pattern[0] == self.X_serach and X_pattern[1] == self.X_serach[::-1]:
            X3 = True
        else:
            X3 = False
        if X_pattern[0] == self.X_serach[::-1] and X_pattern[1] == self.X_serach:
            X4 = True
        else:
            X4 = False

        return X1 or X2 or X3 or X4
    
    def part_two(self):
        result = 0
        for x in range(self.rows):
            for y in range(self.columns):
                if self.check_X(x, y):
                    result += 1
        print(result)
        