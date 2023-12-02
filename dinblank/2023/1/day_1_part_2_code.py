import re

txt_nums = {
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

def allnumbers(line):
    digits = re.findall(r"(?=([0-9]|" + "|".join(list(txt_nums.keys())) + r"))", line)

    first = txt_nums.get(digits[0]) or digits[0]
    last = txt_nums.get(digits[-1]) or digits[-1]

    return int(f"{first}{last}")
def p2sum():
    p2_sum = 0

    with open('day 1 - input2.txt') as file:
        for line in file:
            p2_sum += allnumbers(line)

    print(str(p2_sum))

if __name__ == "__main__":
    
    p2sum()
