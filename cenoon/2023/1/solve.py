#!/usr/bin/python
import re

# define word to digit mappings
WORD_NUMS = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}

def solve_pt1(infile):
    total = 0
    for line in infile:
        # use regex to get all numeric digits and spelled out digits in string
        digits = re.findall('\d', line)

        # accumulate total based on first and last digit
        total += int(digits[0])*10 + int(digits[-1])

    print(total)

def solve_pt2(infile):
    total = 0
    for line in infile:
        # use regex to get all numeric digits and spelled out digits in string
        digits = re.findall('(?=(\d|'+'|'.join(list(WORD_NUMS.keys()))+'))', line)
        
        # convert spelled out digits to numeric
        if digits[0] in WORD_NUMS:
            digits[0] = WORD_NUMS[digits[0]]
        if digits[-1] in WORD_NUMS:
            digits[-1] = WORD_NUMS[digits[-1]]

        # accumulate total based on first and last digit
        total += int(digits[0])*10 + int(digits[-1])

    print(total)

if __name__ == '__main__':
    #with open('./example.txt', 'r') as infile:
    with open('./input.txt', 'r') as infile:
        solve_pt1(infile)
        infile.seek(0)
        solve_pt2(infile)