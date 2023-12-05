# with open("../input") as f:
#     lines = f.readlines()

#     seeds = []
#     attaching_map = ""
#     current_map = {}
#     maps = {}
#     denominator = 1
#     for line in lines:
#         print(line)
#         if line.startswith("seeds:"):
#             seeds = line.split(" ")[1:]
#             for i in seeds:
#                 denominator *= int(i)
#             continue

#         if "map:" in line:
#             attaching_map = line.split(" ")[0]
#             continue

#         if line.replace("\n", "") in ["", " "]:
#             if attaching_map == "":
#                 continue

#             maps[attaching_map] = current_map
#             attaching_map = ""
#             current_map = {}
#             continue

#         destination_start, source_start, range_length = line.split(" ")
#         destination_start = int(destination_start)
#         source_start = int(source_start)
#         range_length = int(range_length)

#         for i in range(range_length):
#             current_map[(source_start + i) % denominator] = (
#                 destination_start + i
#             ) % denominator

#         maps[attaching_map] = current_map

#     minimum_location = -1
#     for seed in seeds:
#         seed = int(seed)
#         soil = maps["seed-to-soil"].get(seed, seed)
#         fertilizer = maps["soil-to-fertilizer"].get(soil, soil)
#         water = maps["fertilizer-to-water"].get(fertilizer, fertilizer)
#         light = maps["water-to-light"].get(water, water)
#         temperature = maps["light-to-temperature"].get(light, light)
#         humidity = maps["temperature-to-humidity"].get(temperature, temperature)
#         location = maps["humidity-to-location"].get(humidity, humidity)
#         if minimum_location == -1 or location < minimum_location:
#             minimum_location = location

#         print(
#             f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}"
#         )

#     print(f"Minimum location: {minimum_location}")


import math
import os, sys
import time

class SeedMap:
    def __init__(self, off: str, to: str):
        self.off = off
        self.to = to
        # mapping values
        # tuple represents (source, max_source, target)
        # source is inclusive, max_source is exclusive
        self.map_values: list[tuple[int, int, int]] = []
    def add(self, target: int, source: int, offset: int):
        self.map_values.append((source, source + offset, target))
    def get_destination(self, given: int):
        # for each mapping range
        for source, max_source, target in self.map_values:
            # if given is in between range
            if source <= given < max_source:
                # map it
                return target + (given - source)
        # if no range was found,
        # return value unchanged
        return given
    def __str__(self) -> str:
        return f"{self.off} => {self.to}"
    def __repr__(self) -> str:
        return self.__str__()


def main():
    with open(os.path.join(sys.path[0],"../input"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    lines = text.split("\n")

    # parse first line to get all seeds
    seeds = [int(s) for s in lines[0].split(": ")[1].split(" ")]
    # create seed maps
    seed_maps: list[SeedMap] = []
    current_map = None
    # for each other line except 1st line
    for line in lines[1:]:
        # skip empty lines
        if line == "":
            continue
        # if new map declaration start
        if line.endswith("map:"):
            # get from and to strings (just for printing)
            off, to = line.split(" ")[0].split("-to-", 1)
            # create new map
            current_map = SeedMap(off, to)
            # and add it to the list
            seed_maps.append(current_map)
        else:
            # if not new map declaration, add the mapping
            # the * will unpack the list into 3 arguments
            current_map.add(*[int(s) for s in line.split(" ")])
    min_location = math.inf
    # for each seed
    for seed in seeds:
        # map it through all seed maps
        for seed_map in seed_maps:
            seed = seed_map.get_destination(seed)
        # and update the minimum location
        min_location = min(min_location, seed)
    print(min_location)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f} seconds")
