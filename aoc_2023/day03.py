class GearRatios():
    def __init__(self, content) :
        self.engine_matrix = content
        self.numbers = []
        self.gears = []

        is_number = False
        number_string = ""
        number_row = 0
        number_column = 0
        for row_index, row in enumerate(self.engine_matrix):
            for column_index, column in enumerate(row):
                if column == "*":
                    self.gears.append(
                        {
                            "row": row_index,
                            "column": column_index
                        }
                    )
                if column.isdigit():
                    if is_number == False:
                        number_string = str(column)
                        number_row = row_index
                        number_column = column_index
                        is_number = True
                    else:
                        number_string = number_string + str(column)
                else:
                    is_number = False
                    if len(number_string) > 0:
                        self.append_number(number_string, number_row, number_column)
                        number_string = ""
            if len(number_string) > 0:
                self.append_number(number_string, number_row, number_column)
                number_string = ""
            
    def append_number(self, string, row, column):
        self.numbers.append(
            {
                "string": string,
                "row": row,
                "column": column
            }
        )

    def startrange(self, num):
        start_range = 0
        if num["column"] > start_range:
            start_range = num["column"] - 1
        return start_range
    
    def endrange(self, num):
        end_range = len(self.engine_matrix[num["row"]]) - 1
        if (num["column"] + len(num["string"])) < end_range:
            end_range = num["column"] + len(num["string"]) + 1
        return end_range
        
    def part_number(self):
        partnumber = 0
        for number in self.numbers:
            number_added = False
            # check left:
            if number["column"] > 0:
                if (self.engine_matrix[number["row"]][number["column"] - 1] != ".") and (not number_added):
                    partnumber = partnumber + int(number["string"])
                    number_added = True
            # check right:
            if (number["column"] + len(number["string"]) + 1) < len(self.engine_matrix[number["row"]]):
                if (self.engine_matrix[number["row"]][number["column"] + len(number["string"])] != ".") and (not number_added):
                    partnumber = partnumber + int(number["string"])
                    number_added = True
            # check above row:
            if number["row"] > 0:
                for i in range(self.startrange(number), self.endrange(number)):
                    if (self.engine_matrix[number["row"] - 1][i] != ".") and (not self.engine_matrix[number["row"] - 1][i].isdigit()) and (not number_added):
                        partnumber = partnumber + int(number["string"])
                        number_added = True
            # check underneath row:
            if number["row"] < len(self.engine_matrix) - 1:
                for i in range(self.startrange(number), self.endrange(number)):
                    if (self.engine_matrix[number["row"] + 1][i] != ".") and (not self.engine_matrix[number["row"] + 1][i].isdigit()) and (not number_added):
                        partnumber = partnumber + int(number["string"])
                        number_added = True

        return partnumber
    
    def gear_ratios(self):
        gearratios = 0
        for gear in self.gears:
            adjacent_numbers = []
            for number in self.numbers:
                # check left:
                if (number["row"] == gear["row"]) and (number["column"] + len(number["string"]) == gear["column"]):
                    adjacent_numbers.append(number)
                # check right:
                if (number["row"] == gear["row"]) and (number["column"] == gear["column"] + 1):
                    adjacent_numbers.append(number)
                # check above row:
                if gear["row"] > 0:
                    if (number["row"] == gear["row"] - 1) and (number["column"] - 1 <= gear["column"]) and (number["column"] + len(number["string"]) >= gear["column"]):
                        adjacent_numbers.append(number)
                # check underneath row:
                if gear["row"] < (len(self.engine_matrix) - 1):
                    if (number["row"] == gear["row"] + 1) and (number["column"] - 1 <= gear["column"]) and (number["column"] + len(number["string"]) >= gear["column"]):
                        adjacent_numbers.append(number)
            if len(adjacent_numbers) == 2:
                gearratios = gearratios + (int(adjacent_numbers[0]["string"]) * int(adjacent_numbers[1]["string"]))
                
        return gearratios
        