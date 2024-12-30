from aoc_2024 import helpers, day01, day02, day03, day04, day05, day06, day07, day13, day14, day15, day16, day18, day19, day24, day25

content = helpers.ContentLoader()

day = 25

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

if day == 13:
    content.set_filename("./aoc_2024/input_13.txt")
    r = day13.ClawContraption(content=content.load())
    r.part_one()
    r.part_two()

if day == 14:
    content.set_filename("./aoc_2024/input_14.txt")
    r = day14.RestroomRedoubt(content=content.load())
    r.part_one_and_two()

if day == 15:
    content.set_filename("./aoc_2024/input_15.txt")
    r = day15.WarehouseWoes(content=content.load())
    r.part_one()

if day == 16:
    content.set_filename("./aoc_2024/input_16_test.txt")
    r = day16.ReindeerMaze(content=content.load())
    r.part_one()

if day == 18:
    content.set_filename("./aoc_2024/input_18.txt")
    r = day18.RAMRun(content=content.load())
    r.part_one()
    r.part_two()

if day == 19:
    content.set_filename("./aoc_2024/input_19.txt")
    r = day19.LinenLayout(content=content.load())
    r.part_one()

if day == 24:
    content.set_filename("./aoc_2024/input_24.txt")
    r = day24.CrossedWires(content=content.load())
    r.part_one()

if day == 25:
    content.set_filename("./aoc_2024/input_25.txt")
    r = day25.CodeChronicle(content=content.load())
    r.part_one()