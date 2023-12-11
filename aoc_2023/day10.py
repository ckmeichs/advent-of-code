class PipeMaze():
    def __init__(self, content) -> None:
        self.grid = []
        for row in content:
            self.grid.append(row)
        self.rows = len(self.grid)
        self.columns = len(self.grid[0])
        self.directions = [
            {"name": "west", "row": 0, "column": -1}, 
            {"name": "north", "row": -1, "column": 0},
            {"name": "east", "row": 0, "column": 1}, 
            {"name": "south", "row": 1, "column": 0}
        ]
        self.pipes = [
            {"pipe": "|", "ways": [self.directions[1], self.directions[3]]},
            {"pipe": "-", "ways": [self.directions[2], self.directions[0]]},
            {"pipe": "L", "ways": [self.directions[1], self.directions[2]]},
            {"pipe": "J", "ways": [self.directions[1], self.directions[0]]},
            {"pipe": "7", "ways": [self.directions[3], self.directions[0]]},
            {"pipe": "F", "ways": [self.directions[3], self.directions[2]]}
        ]
        self.ways = []
        self.enclosed = []
     
    def steps(self):
        start = self.find_start()
        start_points = []
        for direction in self.directions:
            rt = start["row"] + direction["row"]
            ct = start["column"] + direction["column"]
            if (rt >= 0) and (ct >= 0) and not self.grid[rt][ct] == ".":
                pipe = list(filter(lambda i: i["pipe"] == self.grid[rt][ct], self.pipes))[0]
                for way in pipe["ways"]:
                    if direction == self.reverse_direction(way):
                        start_points.append({"dir": direction ,"row": rt, "column": ct})
        
        step_list = []
        for run in start_points:
            this_way = []
            steps = 1
            r = run["row"]
            c = run["column"]
            d = run["dir"]
            
            while self.grid[r][c] != "S":
                this_way.append({"row": r, "column": c, "direction": d["name"]})
                steps += 1
                pipe = list(filter(lambda i: i["pipe"] == self.grid[r][c], self.pipes))[0]
                d = self.reverse_direction(d)
                for direction in pipe["ways"]:
                    if d != direction:
                        r = r + direction["row"]
                        c = c + direction["column"] 
                        d = direction
                        break
                
            step_list.append(steps)
            self.ways.append(this_way)
        
        if len(step_list) == 2 and step_list[0] == step_list[1]:
            return int(step_list[0] / 2)
        else:
            return -1
    
    def find_enclosed(self):
        
        wg = self.print_grid()
        
        # south ---------------------------------------------------------------------
        for step in self.ways[0]:
            if step["direction"] == "south":
                r = step["row"]
                c = step["column"] + 1
                while self.is_in_range(r, c) and wg[r][c] == ".":
                    if not self.enclosed_present(row=r, column=c):
                        self.enclosed.append({"row": r, "column": c})
                    r2 = r - 1
                    while self.is_in_range(r2, c) == ".":
                        if not self.enclosed_present(row=r2, column=c):
                            self.enclosed.append({"row": r2, "column": c})
                        r2 -= 1
                    r2 = r + 1
                    while self.is_in_range(r2, c) and wg[r2][c] == ".":
                        if not self.enclosed_present(row=r2, column=c):
                            self.enclosed.append({"row": r2, "column": c})
                        r2 += 1
                    c += 1
                
                    r = step["row"] + 1
                    c = step["column"] + 1
                    while self.is_in_range(r, c) and wg[r][c] == ".":
                        if not self.enclosed_present(row=r, column=c):
                            self.enclosed.append({"row": r, "column": c})
                        c2 = c + 1
                        while self.is_in_range(r, c2) and wg[r][c2] == ".":
                            if not self.enclosed_present(row=r, column=c2):
                                self.enclosed.append({"row": r, "column": c2})
                            c2 += 1
                        c2 = c - 1
                        while self.is_in_range(r, c2) and wg[r][c2] == ".":
                            if not self.enclosed_present(row=r, column=c2):
                                self.enclosed.append({"row": r, "column": c2})
                            c2 -= 1
                        r += 1
                        
                    r = step["row"] - 1
                    c = step["column"] + 1
                    while self.is_in_range(r, c) and wg[r][c] == ".":
                        if not self.enclosed_present(row=r, column=c):
                            self.enclosed.append({"row": r, "column": c})
                        c2 = c + 1
                        while self.is_in_range(r, c2) and wg[r][c2] == ".":
                            if not self.enclosed_present(row=r, column=c2):
                                self.enclosed.append({"row": r, "column": c2})
                            c2 += 1
                        c2 = c - 1
                        while self.is_in_range(r, c2) and wg[r][c2] == ".":
                            if not self.enclosed_present(row=r, column=c2):
                                self.enclosed.append({"row": r, "column": c2})
                            c2 -= 1
                        r += 1
                     
            # north ---------------------------------------------------------------------              
            if step["direction"] == "north":
                r = step["row"]
                c = step["column"] - 1
                while self.is_in_range(r, c) and wg[r][c] == ".":
                    if not self.enclosed_present(row=r, column=c):
                        self.enclosed.append({"row": r, "column": c})
                    r2 = r - 1
                    while self.is_in_range(r2, c) and wg[r2][c] == ".":
                        if not self.enclosed_present(row=r2, column=c):
                            self.enclosed.append({"row": r2, "column": c})
                        r2 -= 1
                    r2 = r + 1
                    while self.is_in_range(r2, c) and wg[r2][c] == ".":
                        if not self.enclosed_present(row=r2, column=c):
                            self.enclosed.append({"row": r2, "column": c})
                        r2 += 1
                    c -= 1
                
                    r = step["row"] - 1
                    c = step["column"] - 1
                    while self.is_in_range(r, c) and wg[r][c] == ".":
                        if not self.enclosed_present(row=r, column=c):
                            self.enclosed.append({"row": r, "column": c})
                        c2 = c + 1
                        while self.is_in_range(r, c2) and wg[r][c2] == ".":
                            if not self.enclosed_present(row=r, column=c2):
                                self.enclosed.append({"row": r, "column": c2})
                            c2 += 1
                        c2 = c - 1
                        while self.is_in_range(r, c2) and wg[r][c2] == ".":
                            if not self.enclosed_present(row=r, column=c2):
                                self.enclosed.append({"row": r, "column": c2})
                            c2 -= 1
                        r -= 1
                        
                    r = step["row"] + 1
                    c = step["column"] - 1
                    while self.is_in_range(r, c) and wg[r][c] == ".":
                        if not self.enclosed_present(row=r, column=c):
                            self.enclosed.append({"row": r, "column": c})
                        c2 = c + 1
                        while self.is_in_range(r, c2) and wg[r][c2] == ".":
                            if not self.enclosed_present(row=r, column=c2):
                                self.enclosed.append({"row": r, "column": c2})
                            c2 += 1
                        c2 = c - 1
                        while self.is_in_range(r, c2) and wg[r][c2] == ".":
                            if not self.enclosed_present(row=r, column=c2):
                                self.enclosed.append({"row": r, "column": c2})
                            c2 -= 1
                        r -= 1
            
            # east ---------------------------------------------------------------------    
            if step["direction"] == "east":
                r = step["row"] - 1
                c = step["column"] 
                while self.is_in_range(r, c) and wg[r][c] == ".":
                    if not self.enclosed_present(row=r, column=c):
                        self.enclosed.append({"row": r, "column": c})
                    c2 = c + 1
                    while self.is_in_range(r, c2) and wg[r][c2] == ".":
                        if not self.enclosed_present(row=r, column=c2):
                            self.enclosed.append({"row": r, "column": c2})
                        c2 += 1
                    c2 = c - 1
                    while self.is_in_range(r, c2) and wg[r][c2] == ".":
                        if not self.enclosed_present(row=r, column=c2):
                            self.enclosed.append({"row": r, "column": c2})
                        c2 -= 1
                    r -= 1
                    
                r = step["row"] - 1
                c = step["column"] - 1
                while self.is_in_range(r, c) == ".":
                    if not self.enclosed_present(row=r, column=c):
                        self.enclosed.append({"row": r, "column": c})
                    r2 = r - 1
                    while self.is_in_range(r2, c) and wg[r2][c] == ".":
                        if not self.enclosed_present(row=r2, column=c):
                            self.enclosed.append({"row": r2, "column": c})
                        r2 -= 1
                    r2 = r + 1
                    while self.is_in_range(r2, c) and wg[r2][c] == ".":
                        if not self.enclosed_present(row=r2, column=c):
                            self.enclosed.append({"row": r2, "column": c})
                        r2 += 1
                    c -= 1
                    
                r = step["row"] - 1
                c = step["column"] + 1
                while self.is_in_range(r, c) == ".":
                    if not self.enclosed_present(row=r, column=c):
                        self.enclosed.append({"row": r, "column": c})
                    r2 = r - 1
                    while self.is_in_range(r2, c) and wg[r2][c] == ".":
                        if not self.enclosed_present(row=r2, column=c):
                            self.enclosed.append({"row": r2, "column": c})
                        r2 -= 1
                    r2 = r + 1
                    while self.is_in_range(r2, c) and wg[r2][c] == ".":
                        if not self.enclosed_present(row=r2, column=c):
                            self.enclosed.append({"row": r2, "column": c})
                        r2 += 1
                    c -= 1
                    
            # west ---------------------------------------------------------------------      
            if step["direction"] == "west":
                r = step["row"] + 1
                c = step["column"] 
                while self.is_in_range(r, c) and wg[r][c] == ".":
                    if not self.enclosed_present(row=r, column=c):
                        self.enclosed.append({"row": r, "column": c})
                    c2 = c + 1
                    while self.is_in_range(r, c2) and wg[r][c2] == ".":
                        if not self.enclosed_present(row=r, column=c2):
                            self.enclosed.append({"row": r, "column": c2})
                        c2 += 1
                    c2 = c - 1
                    while self.is_in_range(r, c2) and wg[r][c2] == ".":
                        if not self.enclosed_present(row=r, column=c2):
                            self.enclosed.append({"row": r, "column": c2})
                        c2 -= 1
                    r += 1
                    
                r = step["row"] + 1
                c = step["column"] + 1
                while self.is_in_range(r, c) and wg[r][c] == ".":
                    if not self.enclosed_present(row=r, column=c):
                        self.enclosed.append({"row": r, "column": c})
                    r2 = r - 1
                    while self.is_in_range(r2, c) and wg[r2][c] == ".":
                        if not self.enclosed_present(row=r2, column=c):
                            self.enclosed.append({"row": r2, "column": c})
                        r2 -= 1
                    r2 = r + 1
                    while self.is_in_range(r2, c) and wg[r2][c] == ".":
                        if not self.enclosed_present(row=r2, column=c):
                            self.enclosed.append({"row": r2, "column": c})
                        r2 += 1
                    c += 1
                    
        self.print_nest()
        return len(self.enclosed)
            
    
    def find_start(self):
        for y, row in enumerate(self.grid):
            for x, column in enumerate(row):
                if column == "S":
                    return {"row": y, "column": x}
        return {"row": -1, "column": -1}
    
    def reverse_direction(self, direction):
        if direction["name"] == "east":
            return self.directions[0]
        if direction["name"] == "west":
            return self.directions[2]
        if direction["name"] == "north":
            return self.directions[3]
        if direction["name"] == "south":
            return self.directions[1]
        
    def enclosed_present(self, row, column):
        for e in self.enclosed:
            if e["row"] ==row and e["column"] == column:
                return True
        return False
        
    def print_grid(self):
        way_grid = []
        for r in range(0, self.rows):
            way_row = ""
            for c in range(0, self.columns):
                if next(filter(lambda x: x['row'] == r and x['column'] == c, self.ways[0]), None):
                   way_row += "*"
                else:
                    way_row += "."
            way_grid.append(way_row)           
        return way_grid
    
    def print_nest(self):
        for r in range(0, self.rows):
            print(" ")
            for c in range(0, self.columns):
                if next(filter(lambda x: x['row'] == r and x['column'] == c, self.ways[0]), None):
                   print("*", end="")
                elif next(filter(lambda x: x['row'] == r and x['column'] == c, self.enclosed), None):
                   print("I", end="")
                else:
                    print(".", end="")
        print(" ")
  
    def is_in_range(self, r, c):
        if ((r >= 0) and (r <= self.rows )) and ((c >= 0) and (c <= self.columns)):
            return True
        else:
            return False