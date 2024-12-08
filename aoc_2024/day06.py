class GuardGallivant:
    def __init__(self, content):
        self.grid = []
        for line in content:
            self.grid.append(list(line))
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.direction_symbols = {"^": 0, ">": 1, "v": 2, "<": 3}
        self.rows = len(self.grid)
        self.cols = len(content[0])
        self.start_pos = None
        self.start_dir = None
    
    def part_one(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] in self.direction_symbols:
                    self.start_pos = (r, c)
                    self.start_dir = self.direction_symbols[self.grid[r][c]]
                    break
            if self.start_pos:
                break
        visited = set()
        pos = self.start_pos
        direction = self.start_dir
        
        while True:
            visited.add(pos)
            r, c = pos
            dr, dc = self.directions[direction]
            next_pos = (r + dr, c + dc)
            if 0 <= next_pos[0] < self.rows and 0 <= next_pos[1] < self.cols:
                if self.grid[next_pos[0]][next_pos[1]] == "#":
                    direction = (direction + 1) % 4
                else:
                    pos = next_pos
            else:
                break
        print(len(visited))

    def simulate(self, obstruction=None):
        visited = set()
        pos = self.start_pos
        direction = self.start_dir
        if obstruction:
            self.grid[obstruction[0]][obstruction[1]] = "#"
        while True:
            if (pos, direction) in visited:
                if obstruction:
                    self.grid[obstruction[0]][obstruction[1]] = "."
                return True
            visited.add((pos, direction))
            r, c = pos
            dr, dc = self.directions[direction]
            next_pos = (r + dr, c + dc)
            if 0 <= next_pos[0] < self.rows and 0 <= next_pos[1] < self.cols:
                if self.grid[next_pos[0]][next_pos[1]] == "#":
                    direction = (direction + 1) % 4
                else:
                    pos = next_pos
            else:
                if obstruction:
                    self.grid[obstruction[0]][obstruction[1]] = "."
                return False
    
    def part_two(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] in self.direction_symbols:
                    self.start_pos = (r, c)
                    self.start_dir = self.direction_symbols[self.grid[r][c]]
                    break
            if self.start_pos:
                break
        loop_positions = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "." and (r, c) != self.start_pos:
                    if self.simulate(obstruction=(r, c)):
                        loop_positions.add((r, c))
        print(len(loop_positions))
        