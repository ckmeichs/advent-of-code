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

    def rotate(self, area):
        new_area = []
        i = 0
        while i < len(area[0]):
            new_line = ""
            for line in area:
                new_line += line[i]
            i += 1
            new_area.append(new_line)
        return new_area
            
    def summared_notes(self):
        s = 0
        for area in self.areas:                
            j = 0
            while j < len(area) -1 :
                if self.is_mirror(area=area, j=j):
                    s += (j + 1) * 100
                j += 1
            j = 0
            area = self.rotate(area)
            while j < len(area) -1 :
                if self.is_mirror(area=area, j=j):
                    s += (j + 1)
                j += 1
        return s
    
    def is_mirror(self, area, j):
        if area[j] == area[j + 1]:
            m = 1
            is_mirror = True
            while (j - m >= 0) and (j + m + 1 < len(area)):
                if area[j - m] != area[j + m + 1]:
                    is_mirror = False
                m += 1
            if is_mirror:
                return True
        return False
