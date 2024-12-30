class CodeChronicle:
    def __init__(self, content):
        self.lock_patterns = []
        self.lock_codes = []
        self.key_patterns = []
        self.key_codes = []
        key_or_lock = []
        is_key = False
        is_lock = False
        for line in content:
            if line != "":
                if len(set(line)) == 1 and line[0] == "#" and len(key_or_lock) == 0:
                    is_lock = True
                if len(set(line)) == 1 and line[0] == "." and len(key_or_lock) == 0:
                    is_key = True
                key_or_lock.append(line)
            else:
                if is_key:
                    key_or_lock.pop()
                    self.key_patterns.append(key_or_lock)
                    self.key_codes.append(self.get_code_from_pattern(pattern=key_or_lock))
                if is_lock:
                    key_or_lock.pop(0)
                    self.lock_patterns.append(key_or_lock)
                    self.lock_codes.append(self.get_code_from_pattern(pattern=key_or_lock))
                is_key = False
                is_lock = False
                key_or_lock = []
        if is_key:
            key_or_lock.pop()
            self.key_patterns.append(key_or_lock)
            self.key_codes.append(self.get_code_from_pattern(pattern=key_or_lock))
        if is_lock:
            key_or_lock.pop(0)
            self.lock_patterns.append(key_or_lock)
            self.lock_codes.append(self.get_code_from_pattern(pattern=key_or_lock))
        

    def get_code_from_pattern(self, pattern):
        code = []
        for x in range(len(pattern[0])):
            column_code = 0
            for y in range(len(pattern)):
                if pattern[y][x] == "#":
                    column_code += 1
            code.append(column_code)
        return code

    def print_patterns(self):
        print("Keys:")
        for key_code, key_pattern in zip(self.key_codes, self.key_patterns):
            print(key_code)
            for line in key_pattern:
                print(line)
            print("------")
        print("Locks:")
        for lock_code, lock_pattern in zip(self.lock_codes, self.lock_patterns):
            print(lock_code)
            for line in lock_pattern:
                print(line)
            print("-------")
    
    def part_one(self):
        result = 0
        for lock_code, lock_pattern in zip(self.lock_codes, self.lock_patterns):
            for key_code, key_pattern in zip(self.key_codes, self.key_patterns):
                match = True
                if len(lock_pattern) == len(key_pattern):
                    l = len(lock_pattern)      
                else:
                    print("key and lock are not the same size!")
                for lock_column, key_column in zip(lock_code, key_code):
                    if lock_column + key_column >= l:
                        match = False
                if match:
                    result += 1
        print(result)



            
            
    