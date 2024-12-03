import re

class MullItOver:
    def __init__(self, content):
        self.multiply_strings = []
        for line in content:
            self.multiply_strings.append(line)

    def part_one(self):
        result = 0
        for line in self.multiply_strings:
            matches = re.findall(r"mul\((-?\d+),\s*(-?\d+)\)", line)
            for match in matches:
                x, y = match
                result += int(x) * int(y)
        print(result)
    
    def part_two(self):
        result = 0
        do_operation = True
        for line in self.multiply_strings:
            matches = re.finditer(r"(mul\((-?\d+),\s*(-?\d+)\))|(do\(\))|(don't\(\))", line)
            for match in matches:
                if match.group(1):
                    if do_operation:
                        x = int(match.group(2))
                        y = int(match.group(3))
                        result += x * y
                elif match.group(4):
                    do_operation = True
                elif match.group(5):
                    do_operation = False
        print(result)