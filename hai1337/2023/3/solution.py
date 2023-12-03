# """Advent of Code 2023 - Day Two :-)

# Silver:
#     Return: sum of all part numbers. A number is a part number if it is adjacent to a symbol, even diagonally
#     Answer: 550064

# Gold:
#     Return:
#     Answer: 57171436
# """


SPECIAL_CHARS = '!@#$%^&*()-+?_=,<>/"'


def has_adj_symbol(matrix, positions) -> bool:
    """Return True if the given position has an adjacent symbol"""
    for position in positions:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                # X and Y bounds of the matrix
                rangeX = range(len(matrix))
                rangeY = range(len(matrix[0]))

                # calculate the position of the adjacent cell
                (newX, newY) = (position[0] + dx, position[1] + dy)

                # if the position is in the bounds of the matrix and contains a special char, return True
                if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                    if matrix[newX][newY] in SPECIAL_CHARS:
                        return True

    return False


def has_adj_num(matrix, position):
    """Find and return a list of all adjacent numbers"""
    num_pos = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            # X and Y bounds of the matrix
            rangeX = range(len(matrix))  # X bounds
            rangeY = range(len(matrix[0]))  # Y bounds

            # calculate the position of the adjacent cell
            (newX, newY) = (position[0] + dx, position[1] + dy)

            # if the position is in the bounds of the matrix, is a digit, and not already captured, add to the list
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                if matrix[newX][newY].isdigit():
                    if (newX, newY - 1) not in num_pos:
                        num_pos.append((newX, newY))
    return num_pos


def calculate_silver(matrix) -> int:
    """Calculate the sum of all numbers adjacent to a symbol"""
    sum = 0

    for x in range(0, len(matrix)):
        digit = ""
        pos = []

        for y in range(0, len(matrix[0])):
            current_char = matrix[x][y]

            if current_char.isdigit():
                digit += current_char
                pos.append((x, y))

            if digit and not current_char.isdigit():
                if has_adj_symbol(matrix, pos):
                    sum += int(digit)
                digit = ""
                pos = []

    return sum


def get_num(arr, num_pos):
    """(Poorly) get the complete number given a position of a single digit"""
    before = ""
    after = ""
    b = num_pos
    a = num_pos

    while b - 1 >= 0 and arr[b - 1].isdigit():
        before += arr[b - 1]
        b -= 1
    while a <= len(arr) and arr[a + 1].isdigit():
        after += arr[a + 1]
        a += 1

    return f"{before[::-1]}{arr[num_pos]}{after}"


def calculate_gold(matrix):
    """Return the sum of the multiplication of two numbers adjacent to the same *"""
    sum = 0
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            current_char = matrix[x][y]
            # once a * is found, look for adjacent digits
            if current_char == "*":
                num_pos = has_adj_num(matrix, (x, y))
                # if there are exactly two different adj digits, get the full number and add it to the sum
                if len(num_pos) == 2:
                    first = get_num(matrix[num_pos[0][0]], num_pos[0][1])
                    second = get_num(matrix[num_pos[1][0]], num_pos[1][1])
                    sum += int(first) * int(second)

    return sum


if __name__ == "__main__":
    silver_sum = 0
    gold_sum = 0

    # load input as a matrix
    with open("input.txt", "r") as f:
        matrix = [[char for char in line] for line in f]

    silver_sum = calculate_silver(matrix)
    gold_sum = calculate_gold(matrix)

    print("Silver Star Sum: " + str(silver_sum))
    print("Gold Star Sum: " + str(gold_sum))
