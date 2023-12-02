## Globals

color_max = {
    "red": 12,
    "green": 13,
    "blue": 14
}

possible_games = [number for number in range(1, 101)]
set_powers = []


# Read info from input file
with open("input") as file:
    input = file.read()

for line in input.split("\n"):
    
    game_info = line.replace("Game ", "").split(": ")
    game_id = game_info[0]
    game_rounds = game_info[1].split(";")
    color_counts = [count.strip().split(', ') for count in game_rounds]

    # vars for part 2
    color_minimum = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    set_power = 1

    print(f"-----------------------")
    print(f"Game ID: {game_id}")
    print(f"Rounds:  {color_counts}")

    for count in color_counts:
        color_numbers = [color_number.split(" ") for color_number in count]
        for color_number in color_numbers:
            color = color_number[1]
            count = int(color_number[0])

            if count >= color_minimum[color]:
                color_minimum[color] = count

            if count > color_max[color]:
                try: 
                    possible_games.remove(int(game_id))
                except ValueError:
                    pass
    
    
    for color, minimum in color_minimum.items():
        set_power *= minimum

    print(f"Minimum cube numbers: {color_minimum}")
    print(f"Set Power: {set_power}")
    set_powers.append(set_power)

print(f"\nPart 1 Solution")
print(f"Possible games: {possible_games}" )
print(f"Sum of IDs of Possible Game: {sum(possible_games)}")

print(f"\nPart 2 Solution")
print(f"Set Powers: {set_powers}")
print(f"Set Powers: {sum(set_powers)}")