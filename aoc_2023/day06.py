class BoatRace():
    def __init__(self, content) -> None:
        self.times = []
        self.distances = []
        
        for line in content:
            strings = line.split(" ")
            if strings[0] == "Time:":
                for string in strings:
                    if string.isdigit():
                        self.times.append(string)
            else:
                for string in strings:
                    if string.isdigit():
                        self.distances.append(string)
                
    def winning_variants(self):
        variants = 1
        for time, distance in zip(self.times, self.distances):
            this_variants = 0
            for t in range(1, int(time)):
                if ((int(time) - t) * t) > int(distance):
                    this_variants = this_variants + 1
            variants *= this_variants
                    
        return variants
    
    def winning_variants_v2(self):
        variants = 0
        time_string = ""
        distance_string = ""
        for time, distance in zip(self.times, self.distances):
            time_string += time
            distance_string += distance
            
        for t in range(1, int(time_string)):
            if ((int(time_string) - t) * t) > int(distance_string):
                variants += 1
         
        return variants
    