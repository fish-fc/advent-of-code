"""Advent of Code 2023 - Day One :-)
Input: .txt with each line containing a string of random ints and spelled out ints
    Ex: threerznlrhtkjp23mtflmbrzq395three 

Silver:
    Return: Sum of the combination of the first and last int from each line
    Ex: threerznlrhtkjp23mtflmbrzq395three = 25

Gold:
    Return: Sum of the combination of the first and last int and spelled out int 
    Ex: threerznlrhtkjp23mtflmbrzq395three = 33 
"""

import re

NUM_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def calculate_silver(line):
    digits = re.findall("[0-9]", line)

    return int(f"{digits[0]}{digits[-1]}")


def calculate_gold(line):
    digits = re.findall(r"(?=([0-9]|" + "|".join(list(NUM_WORDS.keys())) + r"))", line)

    first = NUM_WORDS.get(digits[0]) or digits[0]
    last = NUM_WORDS.get(digits[-1]) or digits[-1]

    return int(f"{first}{last}")


def get_silver_sum():
    silver_sum = 0

    with open("silver.txt") as file:
        for line in file:
            silver_sum += calculate_silver(line)

    print("Silver Star Sum: " + str(silver_sum))


def get_gold_sum():
    gold_sum = 0

    with open("gold.txt") as file:
        for line in file:
            gold_sum += calculate_gold(line)

    print("Gold Star Sum: " + str(gold_sum))


if __name__ == "__main__":
    get_silver_sum()
    get_gold_sum()
