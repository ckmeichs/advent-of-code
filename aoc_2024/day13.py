import re
from math import gcd
from itertools import product

class ClawContraption:
    def __init__(self, content):
        self.machines = []
        self.values = []
        for line in content:
            matches = re.findall(r"\d+", line)
            for match in matches:
                self.values.append(int(match))
        machines_list = self.split_into_sublists()
        for m in machines_list:
            self.machines.append(tuple(m))


    def split_into_sublists(self):
        return [self.values[i:i + 6] for i in range(0, len(self.values), 6)]
    
    def extended_gcd(self, a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = self.extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y
        
    def solve_claw_machine(self, xA, yA, xB, yB, xP, yP, max_presses):
        gX, xX, yX = self.extended_gcd(xA, xB)
        gY, xY, yY = self.extended_gcd(yA, yB)
        if xP % gX != 0 or yP % gY != 0:
            return None

        xX *= xP // gX
        yX *= xP // gX
        xY *= yP // gY
        yY *= yP // gY

        min_cost = float('inf')
        best_combo = None

        for a in range(max_presses - 1):
            for b in range(max_presses - 1):
                if (a * xA + b * xB == xP) and (a * yA + b * yB == yP):
                    cost = 3 * a + b
                    if cost < min_cost:
                        min_cost = cost
                        best_combo = (a, b)

        return min_cost if best_combo else None
    
    def part_one(self):
        total_cost = 0
        prizes_won = 0

        for machine in self.machines:
            result = self.solve_claw_machine(*machine, max_presses=100)
            if result is not None:
                total_cost += result
                prizes_won += 1

        print(total_cost)

    def solve_claw_machine_2(self, xA, yA, xB, yB, xP, yP):
       # Check feasibility for both equations
        gX, xX, yX = self.extended_gcd(xA, xB)
        gY, xY, yY = self.extended_gcd(yA, yB)

        if xP % gX != 0 or yP % gY != 0:
            return None  # No solution exists

        # Scale solutions to match the prize location
        scaleX = xP // gX
        scaleY = yP // gY
        xX *= scaleX
        yX *= scaleX
        xY *= scaleY
        yY *= scaleY

        # Adjust solutions to minimize cost
        stepX = xB // gX
        stepY = yB // gY

        min_cost = float('inf')
        best_combo = None

        for kX in range(-100000, 100000):  # Adjust range to handle large values
            aX = xX + kX * stepX
            bX = (xP - aX * xA) // xB
            if aX < 0 or bX < 0:
                continue

            for kY in range(-100000, 100000):
                aY = xY + kY * stepY
                bY = (yP - aY * yA) // yB
                if aY < 0 or bY < 0:
                    continue

                if aX == aY and bX == bY:  # Ensure consistency
                    cost = 3 * aX + bX
                    if cost < min_cost:
                        min_cost = cost
                        best_combo = (aX, bX)

        return min_cost if best_combo else None

    def part_two(self):
        self.machines = [
            machine[:4] + (machine[4] + 10000000000000, machine[5] + 10000000000000)
            for machine in self.machines
        ]
        
        total_cost = 0
        prizes_won = 0

        for machine in self.machines:
            result = self.solve_claw_machine_2(*machine)
            if result is not None:
                total_cost += result
                prizes_won += 1
        
        print(total_cost)
