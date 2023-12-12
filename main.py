import datetime
from aoc_2023 import helpers, day01, day02, day03, day04, day05, day06, day07, day08, day09, day10, day11

content = helpers.ContentLoader()

if datetime.datetime.now().date() > datetime.date(2023, 12, 25):
    day = input("choose a day (1 ... 25): ")
else:
    day = datetime.datetime.now().day

if day == 1:
    content.set_filename("./aoc_2023/input_01.txt")
    r = day01.Trebuchet(content=content.load())
    print("Day 01. The calibration value:", r.calibration_value())
    print("Day 01. The second corrected calibration value:", r.corrected_calibration_value())

if day == 2:
    content.set_filename("./aoc_2023/input_02.txt")
    r = day02.CubeConundrum(content=content.load())
    print("Day 02: The sum of the game IDs:", r.possible_games())
    print("Day 02: The sum of the power of the cube sets:", r.required_cubes())

if day == 3:
    content.set_filename("./aoc_2023/input_03.txt")
    r = day03.GearRatios(content=content.load())
    print("Day 03: The missing engine part:", r.part_number())
    print("Day 03: The gear ratios:", r.gear_ratios())

if day == 4:
    content.set_filename("./aoc_2023/input_04.txt")
    r = day04.ScratchCards(content=content.load())
    print("Day 04: The cards points:", r.points())
    print("Day 04: The number of scretchcards:", r.card_matches())

if day == 5:
    content.set_filename("./aoc_2023/input_05.txt")
    r = day05.Seed(content=content.load())
    print("Day 05: The lowest location:", r.lowest_location())
    print("Day 05: The lowest location with lots of seeds:", r.lowest_location_with_lots_of_seeds())

if day == 6:
    content.set_filename("./aoc_2023/input_06.txt")
    r = day06.BoatRace(content=content.load())
    print("Day 06: The product of winning variants:", r.winning_variants())
    print("Day 06: The second product of winning variants:", r.winning_variants_v2())
    
if day == 7:
    content.set_filename("./aoc_2023/input_07.txt")
    r = day07.CamelCards(content=content.load())
    print("Day 07: The total winnings are:", r.total_winnings(joker=False))
    print("Day 07: The total joker winnings are:", r.total_winnings(joker=True))
    
if day == 8:
    content.set_filename("./aoc_2023/input_08.txt")
    r = day08.HauntedWasteland(content=content.load())
    print("Day 08: Required steps:", r.steps())
    print("Day 08: Required steps v2:", r.steps_v2())

if day == 9:
    content.set_filename("./aoc_2023/input_09.txt")
    r = day09.MirageMaintenance(content=content.load())
    print("Day 09: Sum of extrapolated values at the end of each serie:", r.sum_of_extrapolated_values_end())
    print("Day 09: Sum of extrapolated values: at the beginning of ech serie", r.sum_of_extrapolated_values_beginning())
    
if day == 10:
    content.set_filename("./aoc_2023/input_10.txt")
    r = day10.PipeMaze(content=content.load())
    print("Day 10: Steps from the starting position to the farthest point:", r.steps())
    print("Day 10: Tiles are enclosed by the loop:", r.find_enclosed(), "But this is false. :-(")
    
if day == 11:
    content.set_filename("./aoc_2023/input_11.txt")
    r = day11.CosmicExpansion(content=content.load())    
    print("Day 11: The sum of the lengths:", r.sum_of_lengths())
    print("Day 11: The sum of the lengths in rapid expanded space:", r.sum_of_lengths_2())
    
if day == 12:
    print("Day 12: without me.")
    