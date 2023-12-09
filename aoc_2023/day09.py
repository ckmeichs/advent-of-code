class MirageMaintenance():
    def __init__(self,content) -> None:
        self.series = []
        for line in content:
            serie = []
            serie_str = line.split(" ")
            for str in serie_str:
                serie.append(int(str))
            self.series.append(serie)
     
    def sum_of_extrapolated_values_end(self):
        s = 0
        for serie in self.series:
            extrapolator = 0
            for y in self.get_tree(serie=serie):
                y.append(extrapolator + y[-1])
                extrapolator = y[-1]
            s += extrapolator
        return s
    
    def sum_of_extrapolated_values_beginning(self):
        s = 0
        for serie in self.series:
            extrapolator = 0
            for y in self.get_tree(serie=serie):
                y.insert(0, y[0] - extrapolator)
                extrapolator = y[0]
            s += extrapolator
        return s
             
    def get_tree(self, serie):
        series_list = []
        series_list.insert(0, serie)
        current_serie = serie           
        zero_serie = False
        while not zero_serie:
            next_serie = []
            for x in range (0, len(current_serie) - 1):
                next_serie.append(current_serie[x + 1] - current_serie[x])
            series_list.insert(0, next_serie)
            current_serie = next_serie
            zero_serie = self.is_zero(next_serie)
        return series_list
    
    def is_zero(self, serie):
        for z in serie:
            if z != 0:
                return False
        return True
    