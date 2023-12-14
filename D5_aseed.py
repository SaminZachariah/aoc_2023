import re

# input = "sample_inputs/D5_sample_input.txt"
input = "full_inputs/D5_full_input.txt"


class Map:
    def __init__(self, range_tuples):
        self.range_tuples = range_tuples

    def __repr__(self):
        return f"{self.range_tuples}"

    def __getitem__(self, key):
        for tup in self.range_tuples:
            dest, src, span = tup
            if src <= key < src + span:
                return dest + key - src

        return key


str_input = ""

with open(input, "r") as f:
    for line in f:
        str_input += line

almanac = str_input.split("\n\n")
print("-----------------almanac-----------------")
# print(almanac)
print("-----------------almanac-----------------")

seeds = almanac[0].split(":")[1].split()
seeds = [int(seed) for seed in seeds]

mappings = {}

for map in almanac[1:]:
    map = map.split("\n")
    map_name = map[0].replace("map:", "").strip()

    mappings[map_name] = {}

    map_tups = map[1:]
    print("-----------------map_tups-----------------")
    print(map_name)
    print(map_tups)
    map_tups = [[int(n) for n in tup.split()] for tup in map_tups if tup != ""]

    print(map_tups)

    mappings[map_name] = Map(map_tups)

print("-----------------mappings-----------------")
# print(mappings["humidity-to-location"])
print("-----------------mappings-----------------")
locations = []

for seed in seeds:
    soil = mappings["seed-to-soil"][seed]
    fertilizer = mappings["soil-to-fertilizer"][soil]
    water = mappings["fertilizer-to-water"][fertilizer]
    light = mappings["water-to-light"][water]
    temperature = mappings["light-to-temperature"][light]
    humidity = mappings["temperature-to-humidity"][temperature]
    location = mappings["humidity-to-location"][humidity]
    locations.append(location)

print("-----------------locations-----------------")
# print(locations)
print("-----------------locations-----------------")


seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds) - 1, 2)]
print(seed_ranges)

for r in seed_ranges:
    if r[0] <= 1345419958 + 584992388 < r[1]:
        print("easy?")
        print(1345419958 + 584992388)

print(min(locations))

# seeds = {}
# seed_soil = {}
# soil_fertilizer = {}
# fertilizer_water = {}
# water_light = {}
# light_temperature = {}
# temperaure_humidity = {}
# humidity_location = {}
