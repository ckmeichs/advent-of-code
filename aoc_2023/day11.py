class CosmicExpansion():
    def __init__(self, content) -> None:
        self.content = content
        self.load_content()
        self.expansions_factor = 1000000
    
    def load_content(self):
        self.space = []
        self.galaxies = []
        self.galaxy_pairs = []
        for line in self.content:
            self.space.append(line)
            
    def sum_of_lengths(self):
        sum = 0
        self.expand_space()
        self.find_galaxies()
        self.pair_galaxies()
        self.calculate_disrances()
        
        for pair in self.galaxy_pairs:
            sum += pair["distance"]
            
        return sum
    
    def sum_of_lengths_2(self):
        sum = 0
        self.load_content()
        self.find_galaxies()
        self.expand_space_2()
        self.pair_galaxies()
        self.calculate_distances_2()
        for pair in self.galaxy_pairs:
            sum += pair["distance"]

        return sum
         
    def expand_space(self):
        x = 0 
        while x < len(self.space[0]):
            galaxy = False
            for y in range(0, len(self.space)):
                if self.space[y][x] == "#":
                    galaxy = True
            if not galaxy:
                for y in range(0, len(self.space)):
                    self.space[y] = self.space[y][:x] + "." + self.space[y][x:]
                x += 1
            x += 1
               
        y = 0
        while y < len(self.space):
            if not "#" in self.space[y]:
                self.space.insert(y + 1, "." * x)
                y += 1
            y += 1
        
            
    def find_galaxies(self):
        n = 0
        for y in range(0, len(self.space)):
            for x in range(0, len(self.space[y])):
                if self.space[y][x] == "#":
                    self.galaxies.append({"num": n, "y": y, "ey": 0, "x": x, "ex": 0})
                    n += 1
                            
    def pair_galaxies(self):
        for i in range(len(self.galaxies)):
            for j in range(i+1, len(self.galaxies)):
                self.galaxy_pairs.append(
                    {
                        "g1": self.galaxies[i],
                        "g2": self.galaxies[j],
                        "distance": 0
                    }
                )
        
    def calculate_disrances(self):
        for pair in self.galaxy_pairs:
            pair["distance"] = abs(pair["g1"]["x"] - pair["g2"]["x"]) + abs(pair["g1"]["y"] - pair["g2"]["y"])

    def calculate_distances_2(self):
        for pair in self.galaxy_pairs:
            pair["distance"] = abs(pair["g1"]["ex"] - pair["g2"]["ex"]) + abs(pair["g1"]["ey"] - pair["g2"]["ey"])
                            
    def plot_space(self):
        for y in self.space:
            print(y)
            
    def expand_space_2(self):
        x = 0 
        while x < len(self.space[0]):
            galaxy = False
            for y in range(0, len(self.space)):
                if self.space[y][x] == "#":
                    galaxy = True

            for g in self.galaxies:
                if g["x"] > x:
                    if not galaxy:
                        g["ex"] += self.expansions_factor
                    else:
                        g["ex"] += 1
            x += 1
               
        y = 0
        while y < len(self.space):
            for g in self.galaxies:
                if g["y"] > y:
                    if not "#" in self.space[y]:
                        g["ey"] += self.expansions_factor
                    else:
                        g["ey"] += 1
            y += 1
