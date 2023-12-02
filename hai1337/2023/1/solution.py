"""Advent of Code 2023 - Day One :-)
Input: .txt with each line containing a string of random numbers and number words
    Ex: threerznlrhtkjp23mtflmbrzq395three 

Silver:
    Return: Sum of the combination of the first and last number from each line
    Ex: threerznlrhtkjp23mtflmbrzq395three = 25
    Answer: 55971

Gold:
    Return: Sum of the combination of the first and last number or number word 
    Ex: threerznlrhtkjp23mtflmbrzq395three = 33 
    Answer: 54719
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
    digits = re.findall("\d", line)

    return int(f"{digits[0]}{digits[-1]}")


def calculate_gold(line):
    digits = re.findall(r"(?=(\d|" + "|".join(list(NUM_WORDS.keys())) + r"))", line)

    first = NUM_WORDS.get(digits[0]) or digits[0]
    last = NUM_WORDS.get(digits[-1]) or digits[-1]

    return int(f"{first}{last}")


if __name__ == "__main__":
    silver_sum = 0
    gold_sum = 0

    with open("input.txt") as file:
        for line in file:
            gold_sum += calculate_gold(line)
            silver_sum += calculate_silver(line)

    print("Silver Star Sum: " + str(silver_sum))
    print("Gold Star Sum: " + str(gold_sum))
