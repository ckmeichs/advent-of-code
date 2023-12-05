import json

class Seed():
    def __init__(self, content) -> None:
        
        self.seeds = []
        self.seeds_ranges = []
        self.maps = []
        self.current_map = {}
        
        for line in content:
            if line.startswith("seeds:"):
                seeds_string_ist = line.split(" ")
                for seed_string in seeds_string_ist:
                    if seed_string.isdigit():
                        self.seeds.append(int(seed_string))

            if line.endswith("map:"):
                map_name = line.split(" ")[0]
                self.current_map = {
                    "name": map_name,
                    "translation_rules": []
                }

            if line != "":
                if line[0].isdigit():
                    line_parts = line.split(" ")
                    translation_rule = {
                        "source_range_start": int(line_parts[1]),
                        "destination_range_start": int(line_parts[0]),
                        "range_length": int(line_parts[2])
                    }
                    self.current_map["translation_rules"].append(translation_rule)
                      
            if line == "":
                if len(self.current_map) > 0:
                    self.maps.append(self.current_map)
                    self.current_map = {}
                    
        if len(self.current_map) > 0:
            self.maps.append(self.current_map)
            
    def lowest_location(self):
        lowest_loc = 9999999999999999
       
        for seed in self.seeds:
            loc = self.get_location(seed)
            if loc < lowest_loc:
                lowest_loc = loc
        return lowest_loc
    
    def lowest_location_with_lots_of_seeds(self):
        lowest_loc = 9999999999999999
        lowest_seed_range = 0
        lowest_seed_steps = 0
        
        range_number = 0
        for i in range(0, len(self.seeds), 2):
            self.seeds_ranges.append(
                {
                    "id": range_number,
                    "start_number": self.seeds[i],
                    "range": self.seeds[i + 1]
                }
            )
            range_number = range_number + 1
            
        # rough approximation in 1000s increments
        for seed_range in self.seeds_ranges:
            print("check seeds from", seed_range["start_number"], "in range", seed_range["range"])
            steps = 0
            for seed in range(seed_range["start_number"], seed_range["start_number"] + seed_range["range"] - 1, 1000):
                loc = self.get_location(seed)
                if loc < lowest_loc:
                    lowest_loc = loc
                    lowest_seed_range = seed_range["id"]
                    lowest_seed_steps = steps
                steps = steps + 1
        
        # find the lowest number around the approximation     
        if lowest_seed_steps > 0:
            lowest_seed_steps = lowest_seed_steps - 1
        seed_range = self.seeds_ranges[lowest_seed_range]
        
        for seed in range(seed_range["start_number"] + (lowest_seed_steps * 1000), seed_range["start_number"] + (lowest_seed_steps * 1000) + 999):
            loc = self.get_location(seed)
            if loc < lowest_loc:
                lowest_loc = loc
     
        return lowest_loc
    
    def get_location(self, seed):
        value = seed
        for map in self.maps:
            value_changed = False
            for rule in map["translation_rules"]:
                if (value >= rule["source_range_start"]) and (value < rule["source_range_start"] + rule["range_length"]) and (not value_changed):
                    value = rule["destination_range_start"] + (value - rule["source_range_start"])
                    value_changed = True
                    
        return value
        