class Trebuchet():
    def __init__(self, content) -> None:
        self.value = 0
        self.value_2 = 0
        self.digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.content = content

    def calibration_value(self):
        for line in self.content:
            numbers = []
            for character in line:
                if character.isdigit():
                    numbers.append(character)
            line_value_string = numbers[0] + numbers[-1]
            self.value = self.value + int(line_value_string)
        return self.value

    def corrected_calibration_value(self):
        for line in self.content:
            numbers = []
            string_numbers = []

            for digit_string_index, digit_string in enumerate(self.digit_strings):
                # danger! multiple occurrences!
                start_index = 0
                while True:
                    index = line.find(digit_string, start_index)
                    if index == -1:
                        break
                    string_numbers.append(
                        {
                            "number": digit_string_index + 1,
                            "position": index
                        }
                    )
                    start_index = index + 1

            for character_index, character in enumerate(line):
                if character.isdigit():
                    numbers.append(character)
                for string_number in string_numbers:
                    if character_index == string_number["position"]:
                        numbers.append(str(string_number["number"]))
            
            line_value_string = numbers[0] + numbers[-1]
            self.value_2 = self.value_2 + int(line_value_string)
        return self.value_2
