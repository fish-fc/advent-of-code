#!/usr/bin/python
import re

# define word to digit mappings
word_nums = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}

# with open('./example.txt', 'r') as infile:
with open('./input.txt', 'r') as infile:
    total = 0
    for line in infile:
        # use regex to get all numeric digits and spelled out digits in string
        digits = re.findall('(?=(\d|'+'|'.join(list(word_nums.keys()))+'))', line)
        
        # convert spelled out digits to numeric
        if digits[0] in word_nums:
            digits[0] = word_nums[digits[0]]
        if digits[-1] in word_nums:
            digits[-1] = word_nums[digits[-1]]

        # accumulate total based on first and last digit
        total += int(digits[0])*10 + int(digits[-1])
        

    print(total)