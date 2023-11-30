class MaxCalories:
    def __init__(self) -> None:
        self.current_elf = 1
        self.elf_with_max_calories = 1
        self.current_calories = 0
        self.max_calories = 0

        with open("./aoc_2022/input_01.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
        self.lines = lines
        
        for line in self.lines:
            line = line.strip()

            if line == "":
                # new elf, but first check the last one
                if self.current_calories > self.max_calories:
                    self.max_calories = self.current_calories
                    self.elf_with_max_calories = self.current_elf
                # set new elves start parameters
                self.current_elf = self.current_elf + 1
                self.current_calories = 0
            else:
                # add calories to current elves account
                self.current_calories = self.current_calories + int(line)
        
    def result(self):
        return self.max_calories
