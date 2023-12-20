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
            
    def summared_notes(self):
        s = 0
        for area in self.areas:                
            s += self.mirror(area=area) * 100
            s += self.mirror(area=self.rotate(area))
        return s
    
    def summared_corrected_notes(self):
        s = 0
        for area in self.areas:                
            s += self.mirror(area=area, fix=True) * 100
            s += self.mirror(area=self.rotate(area), fix=True) 
        return s
    
    def mirror(self, area, fix =False):
        j = 0
        fixed = False
        while j < len(area) -1:
            a1 = area[j]
            a2 = area[j + 1]
            if fix and not fixed:
                fixed, a1, a2 = self.correct_blind(a1, a2)
            if a1 == a2:
                m = 1
                ism = True
                while (j - m >= 0) and (j + m + 1 < len(area)):
                    b1 = area[j - m]
                    b2 = area[j + m + 1]
                    if fix and not fixed:
                        fixed, b1, b2 = self.correct_blind(b1, b2)
                    if b1 != b2:
                        ism = False
                    m += 1
                if ism:
                    return j + 1
            j += 1
        return 0
    
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
    
    def correct_blind(self, l1, l2):
        d = []
        f = False
        for i, (ch1, ch2) in enumerate(zip(l1, l2)):
            if ch1 != ch2:
                d.append(i)
        if len(d) == 1:
            l1 = l1[:d[0]] + l2[d[0]] + l1[d[0]+1:]
            f = True
        return f, l1, l2

