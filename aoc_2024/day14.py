import re, os, time

class RestroomRedoubt:
    def __init__(self, content):
        self.rx = 100
        self.ry = 102
        self.robots = []
        for line in content:
            numbers = re.findall(r"-?\d+", line)
            ints = list(map(int, numbers))
            robot = {
                "px": ints[0],
                "py": ints[1],
                "sx": ints[2],
                "sy": ints[3]
            }
            self.robots.append(robot)

    def visualize(self):
        is_pattern = False
        room = []
        for y in range(self.ry):
            line = ""
            for x in range(self.rx):
                is_a_robot_there = False
                for robot in self.robots:
                    if robot["py"] == y and robot["px"] == x:
                        is_a_robot_there = True
                if is_a_robot_there:
                    line += "*"
                else:
                    line += " "
            room.append(line)
            if "***********" in line:
                is_pattern = True
        if is_pattern:
            for line in room:
                print(line)
            input()
  
    def part_one_and_two(self):
        for i in range(100000000000):
            print(i)
            for robot in self.robots:
                robot["px"] = robot["px"] + robot["sx"]
                robot["py"] = robot["py"] + robot["sy"]
                if robot["px"] < 0:
                    robot["px"] = robot["px"] + self.rx + 1
                if robot["px"] > self.rx:
                    robot["px"] = robot["px"] - self.rx - 1
                if robot["py"] < 0:
                    robot["py"] = robot["py"] + self.ry + 1
                if robot["py"] > self.ry:
                    robot["py"] = robot["py"] - self.ry - 1
            self.visualize()

        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        for robot in self.robots:
            # quadrant 1
            if robot["px"] >= 0 and robot["px"] < self.rx / 2 and robot["py"] >= 0 and robot["py"] < self.ry / 2:
                q1 += 1
            # quadrant 2
            if robot["px"] > self.rx / 2 and robot["px"] <= self.rx  and robot["py"] >= 0 and robot["py"] < self.ry / 2:
                q2 += 1
            # quadrant 3
            if robot["px"] >= 0 and robot["px"] < self.rx / 2 and robot["py"] > self.ry / 2 and robot["py"] <= self.ry:
                q3 += 1
            # quadrant 4
            if robot["px"] > self.rx / 2 and robot["px"] <= self.rx  and robot["py"] > self.ry / 2 and robot["py"] <= self.ry:
                q4 += 1

        print(q1 * q2 * q3 * q4)
