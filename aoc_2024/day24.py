class CrossedWires:
    def __init__(self, content):
        self.gate_types = ["AND", "OR", "XOR"]
        input_segment = 1
        self.gates = []
        self.wires = []
        for line in content[::-1]:
            if line == "":
                input_segment = 2
            elif input_segment == 1:
                gate = line.split(" ")
                gate.pop(3)
                self.gates.append(gate)
                for element in gate:
                    if element not in self.gate_types:
                        wire = {
                            "name": element,
                            "state": None
                        }
                        self.wires.append(wire) 
            elif input_segment == 2:
                signal = line.split(": ")
                for wire in self.wires:
                    if signal[0] == wire["name"]:
                        wire["state"] = bool(int(signal[1]))

    def all_z_wires_set(self):
        for wire in self.wires:
            if wire["name"].startswith("z"):
                if wire["state"] == None:
                    return False
        return True

    def part_one(self):  
        while not self.all_z_wires_set():
            for gate in self.gates:
                value0 = next((item for item in self.wires if item["name"] == gate[0]), None)["state"] 
                value1 = next((item for item in self.wires if item["name"] == gate[2]), None)["state"] 
                result = None
                if (value0 != None) and (value1 != None):
                    if gate[1] == "AND":
                        result = value0 and value1
                    if gate[1] == "OR":
                        result = value0 or value1
                    if gate[1] == "XOR":
                        result = value0 ^ value1
                    item = next((item for item in self.wires if item["name"] == gate[3]), None)
                    if item:
                        item["state"] = result
        
        z_wires = []
        binary_list = []
        for wire in self.wires:
            if wire["name"].startswith("z"):
                z_wires.append(wire)
        sorted_z_wires = sorted(z_wires, key=lambda x: int(x["name"].replace("z", "")), reverse=True)
        for wire in sorted_z_wires:
            binary_list.append(wire["state"])
        binary_str = ''.join('1' if bit else '0' for bit in binary_list)
        print(int(binary_str, 2))
        