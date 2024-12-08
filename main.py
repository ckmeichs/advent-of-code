from aoc_2024 import helpers, day01, day02, day03, day04, day05, day06, day07

content = helpers.ContentLoader()

day = 6

if day == 1:
    content.set_filename("./aoc_2024/input_01.txt")
    r = day01.ChiefHistorian(content=content.load())
    r.part_two()

if day == 2:
    content.set_filename("./aoc_2024/input_02.txt")
    r = day02.RedNosedReports(content=content.load())
    r.part_one()
    r.part_two()

if day == 3:
    content.set_filename("./aoc_2024/input_03.txt")
    r = day03.MullItOver(content=content.load())
    r.part_one()
    r.part_two()

if day == 4:
    content.set_filename("./aoc_2024/input_04.txt")
    r = day04.CeresSearch(content=content.load())
    r.part_one()
    r.part_two()

if day == 5:
    content.set_filename("./aoc_2024/input_05.txt")
    r = day05.PrintQueue(content=content.load_as_text())
    r.part_one()
    r.part_two()

if day == 6:
    content.set_filename("./aoc_2024/input_06.txt")
    r = day06.GuardGallivant(content=content.load())
    r.part_one()
    r.part_two()

if day == 7:
    content.set_filename("./aoc_2024/input_07.txt")
    r = day07.BridgeRepair(content=content.load())
    r.part_one()
    r.part_two()
