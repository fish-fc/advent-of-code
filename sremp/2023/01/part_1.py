## Globals

# represents the sum of all calibration values that are added in the main loop
calibration_sum = 0

# Extract the digits from a given line, returning only the first and last digits found
def extract_calibration_value(line): 
    digits = "".join(c for c in line if c.isdigit())

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