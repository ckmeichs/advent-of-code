class WarehouseWoes:
    def __init__(self, content):
        self.warehouse = []
        self.robot_route = []
        self.robot_pos = {
            "x": 0,
            "y": 0
        }
        input_segment = 1
        y = 0
        for line in content:
            if line == "":
                input_segment = 2
            if input_segment == 1:
                x = 0
                whl = []
                for char in line:
                    if char == "@":
                        self.robot_pos = {
                            "x": x,
                            "y": y
                        }
                    whl.append(char)
                    x += 1
                y +=1
                self.warehouse.append(whl)
            if input_segment == 2:
                for char in line:
                    self.robot_route.append(char)
        
    def print_warehouse(self):
        for y in self.warehouse:
            for x in y:
                print(x, end='')
            print('')

    def check_box(self, direction, x, y):
        num_boxes_in_line = 0
        if direction == "^":
            while self.warehouse[y][x] == "O":
                num_boxes_in_line += 1
                y -= 1
        if direction == "v":
            while self.warehouse[y][x] == "O":
                num_boxes_in_line += 1
                y += 1
        if direction == "<":
            while self.warehouse[y][x] == "O":
                num_boxes_in_line += 1
                x -= 1
        if direction == ">":
            while self.warehouse[y][x] == "O":
                num_boxes_in_line += 1
                x += 1
        if self.warehouse[y][x] == ".":
            moveable = True
        if self.warehouse[y][x] == "#":
            moveable = False
        res = {
            "moveable": moveable,
            "boxes_in_line": num_boxes_in_line
        }
        return res
    
    def move_boxes(self, direction, boxes, x, y):
        if direction == "^":
            self.warehouse[y - boxes][x] = "O"
        if direction == "v":
            self.warehouse[y + boxes][x] = "O"
        if direction == "<":
            self.warehouse[y][x - boxes] = "O"
        if direction == ">":
            self.warehouse[y][x + boxes] = "O"

    def part_one(self):
        for direction in self.robot_route:
            if direction == "^":
                new_x = self.robot_pos["x"]
                new_y = self.robot_pos["y"] - 1
            if direction == "v":
                new_x = self.robot_pos["x"]
                new_y = self.robot_pos["y"] + 1
            if direction == "<":
                new_x = self.robot_pos["x"] - 1
                new_y = self.robot_pos["y"]
            if direction == ">":
                new_x = self.robot_pos["x"] + 1
                new_y = self.robot_pos["y"]
            if self.warehouse[new_y][new_x] == ".":
                self.warehouse[self.robot_pos["y"]][self.robot_pos["x"]] = "."
                self.robot_pos["x"] = new_x
                self.robot_pos["y"] = new_y
                self.warehouse[self.robot_pos["y"]][self.robot_pos["x"]] = "@"
            if self.warehouse[new_y][new_x] == "O":
                check =self.check_box(direction=direction, x=new_x, y=new_y)
                if check["moveable"]:
                    self.warehouse[self.robot_pos["y"]][self.robot_pos["x"]] = "."
                    self.robot_pos["x"] = new_x
                    self.robot_pos["y"] = new_y
                    self.warehouse[self.robot_pos["y"]][self.robot_pos["x"]] = "@"
                    self.move_boxes(direction=direction, boxes=check["boxes_in_line"], x=new_x, y=new_y)
    
        result = 0
        for y in range(len(self.warehouse)):
            for x in range(len(self.warehouse[y])):
                if self.warehouse[y][x] == "O":
                    result += (100 * y + x)

        print(result)    