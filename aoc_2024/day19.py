class LinenLayout:
    def __init__(self, content):
        self.towel_patterns = []
        self.designs = []
        input_segment = 1
        for line in content:
            if line == "":
                input_segment = 2
            elif input_segment == 1:
                self.towel_patterns = line.split(", ")
            elif input_segment == 2:
                self.designs.append(line)

    def can_form_design(self, design):
        if not design:
            return True
        for pattern in self.towel_patterns:
            if design.startswith(pattern):
                if self.can_form_design(design[len(pattern):]):
                    return True
        return False
    
    def part_one(self):
        result = 0
        for design in self.designs:
            print("try:", design)
            if self.can_form_design(design = design):
                result += 1
        
        print(result)
        


            
