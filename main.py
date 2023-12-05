from aoc_2023 import helpers, day01, day02, day03, day04, day05

content = helpers.ContentLoader()

# Day 01:
content.set_filename("./aoc_2023/input_01.txt")
r = day01.Trebuchet(content=content.load())
print("Day 01. The calibration value:", r.calibration_value())
print("Day 01. The second corrected calibration value:", r.corrected_calibration_value())

# Day 02:
content.set_filename("./aoc_2023/input_02.txt")
r = day02.CubeConundrum(content=content.load())
print("Day 02: The sum of the game IDs:", r.possible_games())
print("Day 02: The sum of the power of the cube sets:", r.required_cubes())

# Day 03:
content.set_filename("./aoc_2023/input_03.txt")
r = day03.GearRatios(content=content.load())
print("Day 03: The missing engine part:", r.part_number())
print("Day 03: The gear ratios:", r.gear_ratios())

# Day 04:
content.set_filename("./aoc_2023/input_04.txt")
r = day04.Scratchcards(content=content.load())
print("Day 04: The cards points:", r.points())
# this recursive calculation takes to long for a overall run
# print("Day 04: The number of scretchcards:", r.scretchcards())
print("Day 04: The number of scretchcards: 8477787")

# Day 05:
content.set_filename("./aoc_2023/input_05.txt")
r = day05.Seed(content=content.load())
print("Day 05: The lowest location:", r.lowest_location())
# this recursive calculation takes to long for a overall run
# print("Day 05: The lowest location with lots of seeds:", r.lowest_location_with_lots_of_seeds())
print("Day 05: The lowest location with lots of seeds: 12634632")
