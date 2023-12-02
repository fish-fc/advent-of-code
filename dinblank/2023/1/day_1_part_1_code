
calibration_values_sum = []

with open('day 1 - input2.txt') as input_file:
    for line in input_file:
        numbers = []
        
        for char in line:
            if char.isdigit():
                numbers.append(char) 
        if len(numbers) >= 2:
            sum_numbers = str(numbers[0] + numbers[-1])
            print(sum_numbers)
        else:
            sum_numbers = str(numbers[0] + numbers[0])

        calibration_values_sum.append(int(sum_numbers))
        print(numbers)

print(sum(calibration_values_sum))

