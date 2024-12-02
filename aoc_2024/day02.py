class RedNosedReports:
    def __init__(self, content):
        self.reports = []
        for row in content:
            levels = row.split(" ")
            report = []
            for level in levels:
                report.append(int(level))
            self.reports.append(report)
    
    def check_report(self, report):
        if report[0] > report[-1]:
            dir = "decreasing"
        else:
            dir = "increasing"
        for i in range(len(report) - 1):
            current_level = report[i]
            next_level = report[i+1]
            if dir == "increasing":
                if not(current_level < next_level and (next_level - current_level) < 4):
                    return i
            if dir == "decreasing":
                if not(current_level > next_level and (current_level - next_level) < 4):
                    return i
        return -1

    def part_one(self):
        valid_reports = 0
        for report in self.reports:
            if self.check_report(report=report) == -1:
                valid_reports += 1
        print(valid_reports)

    def part_two(self):
        valid_reports = 0
        for report in self.reports:
            r = self.check_report(report=report)
            if r == -1:
                valid_reports += 1
            else:
                original_report = report
                report.pop(r)
                if self.check_report(report=report) == -1:
                    valid_reports += 1
                else:
                    try:
                        original_report.pop(r + 1)
                    except:
                        pass
                    if self.check_report(report=original_report) == -1:
                        valid_reports += 1
        print(valid_reports)
