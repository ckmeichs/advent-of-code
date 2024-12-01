class ChiefHistorian:
    def __init__(self, content):
        l1 = []
        l2 = []
        for row in content:
            parts = row.split("   ")
            l1.append(int(parts[0]))
            l2.append(int(parts[1]))
        self.sl1 = sorted(l1)
        self.sl2 = sorted(l2)
        result = 0
        for i, j in zip(self.sl1, self.sl2):
            result += abs(i - j)
        print(result)
    
    def part_two(self):
        result = 0
        for i in self.sl1:
            multi = self.sl2.count(i)
            result += (i * multi)
        print(result)


    

