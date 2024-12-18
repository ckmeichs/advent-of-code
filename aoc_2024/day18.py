from collections import deque

class RAMRun:
    def __init__(self, content):
        self.content = content
        self.rx = 71
        self.ry = 71
        self.start = (0,0)
        self.goal = (self.rx - 1, self.ry - 1)
        
    def inizialize_array(self):
        self.array = [["." for _ in range(self.rx)] for _ in range(self.ry)]

    def set_array(self, l):
        self.inizialize_array()
        for i in range(l):
            ps = self.content[i].split(",")
            self.array[int(ps[1])][int(ps[0])] = "#"

    def print_labyrinth(self):
        for y in self.array:
            print(y)
    
    def shortest_path(self):
        rows, cols = self.ry, self.rx
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(self.start, [self.start])])
        visited = set([self.start])
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == self.goal:
                return path
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and self.array[nx][ny] == "." and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
        return None
    
    def part_one(self):
        self.set_array(l=1024)
        self.print_labyrinth()
        path = self.shortest_path()
        if path:
            for pos in path:
                x, y = pos
                self.array[x][y] = "O"
            print(len(path) - 1)
        else:
            print("no way")

    def part_two(self):
        for i in range(len(self.content)):
            self.set_array(l=i + 1)
            
            path = self.shortest_path()
            if not path:
                print(self.content[i])
                break
