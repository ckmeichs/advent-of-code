from math import lcm

class HauntedWasteland():
    def __init__(self, content) -> None:
        self.nodes = []
        self.instructions_sequence = content[0]
        del content[0:2]
        
        for line in content:
            node = {
                "name": line[0:3],
                "L": line[7:10],
                "R": line[12:15]
            }
            self.nodes.append(node)
    
    def steps(self):
        s = 0
        instruction_index = 0
        node = list(filter(lambda x: x["name"] == "AAA", self.nodes))[0]
        
        while node["name"] != "ZZZ":
            instruction = self.instructions_sequence[instruction_index]
            node = list(filter(lambda x: x["name"] == node[instruction], self.nodes))[0]
            s += 1
            instruction_index += 1
            if instruction_index == len(self.instructions_sequence):
                instruction_index = 0
        return s
    
    def steps_v2(self):
        steps_per_run = []
        running_nodes = []
        
        for node in self.nodes:
            if node["name"].endswith("A"):
                running_nodes.append(node)
                
        for node in running_nodes:
            s = 0
            instruction_index = 0
            while not node["name"].endswith("Z"):
                instruction = self.instructions_sequence[instruction_index]
                node = list(filter(lambda x: x["name"] == node[instruction], self.nodes))[0]
                s += 1
                instruction_index += 1
                if instruction_index == len(self.instructions_sequence):
                    instruction_index = 0    
            steps_per_run.append(s)
        return lcm(*steps_per_run)
        