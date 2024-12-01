from aoc_2024 import helpers, day01

content = helpers.ContentLoader()

day = 1

if day == 1:
    content.set_filename("./aoc_2024/input_01.txt")
    r = day01.ChiefHistorian(content=content.load())
    r.part_two()
