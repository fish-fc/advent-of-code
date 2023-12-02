"""Advent of Code 2023 - Day Two :-)
Input: .txt with each line containing containing the following
    Game {game_id}: int {color_1}, int {color_2}; int {color_3}

Silver:
    Return: Sum of game IDs that were possible with a total of 12 red cubes, 13 green cubes, and 14 blue cubes.
    Answer: 2795

Gold:
    Return: Sum of the power of the minimum color of each cubes needed for each game
    Answer: 75561
"""
import re
import math

MAX_CUBES = {"red": 12, "green": 13, "blue": 14}


def split_line(line):
    game_id, cubes = line.removeprefix("Game ").split(": ")

    return int(game_id), cubes


def calculate_silver(line):
    game_id, cubes = split_line(line)

    possible = list(
        (int(number) <= MAX_CUBES.get(color))
        for number, color in (
            element.split(" ") for element in re.split("; |, ", cubes.strip())
        )
    )

    return game_id if False not in possible else 0


def calculate_gold(line):
    current_max = {"blue": 1, "red": 1, "green": 1}
    _, cubes = split_line(line)

    for number, color in (
        element.split(" ") for element in re.split("; |, ", cubes.strip())
    ):
        current_max[color] = max(int(number), int(current_max[color]))

    power = math.prod(current_max.values())

    return int(power)


if __name__ == "__main__":
    silver_sum = 0
    gold_sum = 0

    with open("input.txt") as file:
        for line in file:
            silver_sum += calculate_silver(line)
            gold_sum += calculate_gold(line)

    print("Silver Star Sum: " + str(silver_sum))
    print("Gold Star Sum: " + str(gold_sum))
