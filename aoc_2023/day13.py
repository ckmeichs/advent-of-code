class PointOfIncidence():
    def __init__(self, content) -> None:
        fileds = []
        self.areas = []
        for line in content:
            fileds.append(line)
        y = 0
        this_area = []
                
        while y < len(fileds):
            if content[y] == "":
                self.areas.append(this_area)
                this_area = []
            else:
                this_area.append(content[y])
            y += 1
        self.areas.append(this_area)

    def rotate(self, field):
        new_field = []
        i = 0
        while i < len(field[0]):
            new_line = ""
            for line in field:
                new_line += line[i]
            i += 1
            new_field.append(new_line)
        return new_field
            
    def summared_notes(self):
        s = 0

        for area in self.areas:                
            j = 0
            while j < len(area) -1 :
                if area[j] == area[j + 1]:
                    m = 1
                    is_mirror = True
                    while (j - m >= 0) and (j + m + 1 < len(area)):
                        if area[j - m] != area[j + m + 1]:
                            is_mirror = False
                        m += 1
                    if is_mirror:
                        s += (j + 1) * 100
                j += 1
            j = 0
            area = self.rotate(area)
            while j < len(area) -1 :
                if area[j] == area[j + 1]:
                    m = 1
                    is_mirror = True
                    while (j - m >= 0) and (j + m + 1 < len(area)):
                        if area[j - m] != area[j + m + 1]:
                            is_mirror = False
                        m += 1
                    if is_mirror:
                        s += (j + 1)
                j += 1
        return s
