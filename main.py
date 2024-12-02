from aoc_2024 import helpers, day01, day02

content = helpers.ContentLoader()

day = 2

if day == 1:
    content.set_filename("./aoc_2024/input_01.txt")
    r = day01.ChiefHistorian(content=content.load())
    r.part_two()

if day == 2:
    content.set_filename("./aoc_2024/input_02.txt")
    r = day02.RedNosedReports(content=content.load())
    r.part_one()
    r.part_two()

