import itertools

class BridgeRepair:
    def __init__(self, content):
        self.formulas = [] 
        for line in content:
            parts = line.split(': ')
            numbers = parts[1].split(" ")
            formula = {
                'result': parts[0],
                'numbers': numbers
            }
            self.formulas.append(formula)
        self.operators = ['*', '+']
        self.operators_part_two = ['*', '+', '||']

    def eval_left_to_right(self, expression):
        # We are not allowed to follow the correct mathematical rule 
        # "POINT CALCULATION BEFORE DIRECTION CALCULATION" but have to 
        # calculate from left to right. What kind of nonsense is that?
        tokens = expression.split()
        result = int(tokens[0])
        i = 1
        while i < len(tokens):
            operator = tokens[i]
            operand = int(tokens[i + 1])
            if operator == "+":
                result += operand
            elif operator == "*":
                result *= operand
            i += 2
        return result

    def part_one(self):
        result = 0
        for formula in self.formulas:
            validate = False
            n = len(formula['numbers']) - 1
            combinations = list(itertools.product(self.operators, repeat=n))
            for combination in combinations:
                formula_right = ""
                for i in range(n):
                    formula_right += formula['numbers'][i] + " "
                    formula_right += combination[i] + " "
                formula_right += formula['numbers'][i + 1]
                if int(formula['result']) == self.eval_left_to_right(formula_right):
                    validate = True
            if validate:
                result += int(formula['result'])
        print(result)

    def custom_calculator(self, expression):
        tokens = expression.split()
        result = int(tokens[0])  # Start mit der ersten Zahl
        i = 1
        while i < len(tokens):
            operator = tokens[i]
            operand = int(tokens[i + 1])
            if operator == "+":
                result += operand
            elif operator == "*":
                result *= operand
            elif operator == "||":
                result = int(str(result) + str(operand))
            else:
                raise ValueError(f"Unbekannter Operator: {operator}")
            i += 2
        return result
    
    def part_two(self):
        result = 0
        for formula in self.formulas:
            validate = False
            n = len(formula['numbers']) - 1
            combinations = list(itertools.product(self.operators_part_two, repeat=n))
            for combination in combinations:
                formula_right = ""
                for i in range(n):
                    formula_right += formula['numbers'][i] + " "
                    formula_right += combination[i] + " "
                formula_right += formula['numbers'][i + 1]
                if int(formula['result']) == self.custom_calculator(formula_right):
                    validate = True
            if validate:
                result += int(formula['result'])
        print(result)
