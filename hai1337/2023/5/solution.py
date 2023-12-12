"""Advent of Code Day 5


Silver: Find the closest location that corresponds to the given seeds
    Answer: 340994526

Gold: Find the closest location that corresponds to the given seed ranges
    Answer: 52210644
"""

import re
from pydantic import BaseModel
import math
import pathlib


class Map(BaseModel):
    """A map of each almanac category

    Attr:
        map_category (str): the title of the category, for example, seed-to-soil
        map_values (list): a list of tuples, for example, 1383244180 2567207479 366571891
    """

    map_category: str
    map_values: list[tuple[int, int, int]] = []

    def add_map_values(self, dest: int, source: int, offset: int):
        self.map_values.append((source, source + offset, dest))

    def get_dest(self, given: int):
        # for each range, check if the given is in the range, if it is return its mapped dest, if not, return it unmapped
        for source, max_source, dest in self.map_values:
            if source <= given < max_source:
                return dest + (given - source)
        return given

    def get_range_min(self, seeds: list):
        i = 0
        seed_map = seeds
        while i < len(seeds):
            f = False
            seed_start, seed_end = seeds[i]
            for dest, source, range in self.map_values:
                if (
                    seed_start >= source
                    and seed_start < (source + range)
                    and f == False
                ):
                    f = True
                    seed_map[i][0] = dest + (seed_start - source)
                    if seed_end < source + range:
                        seed_map[i][1] = dest + (seed_end - source)
                    else:
                        seed_map[i][1] = dest + range - 1
                        seed_map.append([source + range, seed_end])

                elif seed_end >= source and seed_end < (source + range) and f == False:
                    f = True
                    seed_map[i][1] = source + (seed_end - source)
                    if seed_start > source:
                        seed_map[i][0] = dest + (seed_start - source)
                    else:
                        seed_map[i][0] = dest
                        seed_map.append([seed_start, source - 1])
            i += 1
        return seed_map


def create_maps(text_list):
    maps: list[Map] = []
    current_map = None

    # loop through every line except the first line
    for line in text_list[1:]:
        # create a new map with category and values
        current_map = Map(map_category=line[0].split(" ")[0])
        maps.append(current_map)
        
        for i in line[1:]:
            current_map.add_map_values(*[int(s) for s in i.split(" ")])
    
    return maps


def find_minimum(seeds, maps):
    min_location = math.inf

    # for each seed, run it through the  maps and update the minimum location
    for seed in seeds:
        for _map in maps:
            seed = _map.get_dest(seed)
        min_location = min(min_location, seed)
    return min_location


def seed_locations(seeds, maps):
    for _map in maps:
        seeds + _map.get_range_min(seeds)
    return min(min(s) for s in seeds)


if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read().strip()

    text_list = [line.split("\n") for line in text.split("\n\n")]

    # Create a list of seeds from the first line
    silver_seeds = [int(s) for s in text_list[0][0].split(": ")[1].split(" ")]
    seed_ranges = [
        (int(silver_seeds[i]), int(silver_seeds[i + 1]))
        for i in range(0, len(silver_seeds), 2)
    ]
    seed_list = [int(seed) for seed in text_list[0][0].split(":")[1].split()]
    seeds = [
        [seed_list[a], seed_list[a] + seed_list[a + 1] - 1]
        for a in range(0, len(seed_list), 2)
    ]

    maps = create_maps(text_list)

    silver_answer = find_minimum(silver_seeds, maps)
    gold_answer = seed_locations(seeds, maps)

    print("Silver Star Answer: " + str(silver_answer))
    print("Gold Star Answer: " + str(gold_answer))
