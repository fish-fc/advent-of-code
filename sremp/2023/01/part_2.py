## Globals

# represents the sum of all calibration values that are added in the main loop
calibration_sum = 0

# (for part 2) map the string expressions of digits to their corresponding numeric characters
digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# Translate digits and extract them to a list, returning only the first and last digits that were found
def extract_calibration_value(line): 

    for digit_name, digit in digit_map.items():
        # Need to pad the digit names in order to avoid overlapping characters edge case
        # Ex. "eightwothree" - the eight will get thrown out in a standard replacement
        line = line.replace(digit_name, f"{digit_name}{digit}{digit_name}")

    digits = [c for c in line if c.isnumeric()]

    return digits[0] + digits[-1]


# Read the calibration doc provided by AoC
with open("calibration_doc") as file:
    calibration_doc = file.read()


# Go through every line in the doc, extract the calibration values and add to sum
for line in calibration_doc.strip().split("\n"):
    calibration_value = extract_calibration_value(line)
    calibration_sum += int(calibration_value)

    print(f"Line: {line}")
    print(f"Calibration value: {calibration_value}")
    print(f"Current total: {calibration_sum}\n-------")

print(calibration_sum)