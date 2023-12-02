#!/usr/bin/python
import math

def solve_pt1(infile):
    red_max = 12
    green_max = 13
    blue_max = 14
    total = 0
    for line in infile: 
        valid = True

        # get selections parsed into game ID and color values
        game_id = line.split(':')[0].split(' ')[1]
        selections = line.split(':')[1].strip().replace(';', ',').split(',')
        selections = [selection.strip().split(' ') for selection in selections]
        
        for selection in selections:
            if (selection[1] == 'red' and int(selection[0]) > red_max) \
            or (selection[1] == 'green' and int(selection[0]) > green_max) \
            or (selection[1] == 'blue' and int(selection[0]) > blue_max):
                valid = False

        if valid:
            total += int(game_id)
    print(total)


def solve_pt2(infile):
    total = 0

    for line in infile: 
        color_max = {'red':0, 'green':0, 'blue':0}
        # get selections parsed into game ID and color values
        selections = line.split(':')[1].strip().replace(';', ',').split(',')
        selections = [selection.strip().split(' ') for selection in selections]
        
        # get the max of each color present
        for selection in selections:
            if color_max[selection[1]] < int(selection[0]):
                color_max[selection[1]] = int(selection[0])
        
        # generate powers and accumulate total
        power = math.prod(color_max.values())
        total += power

    print(total)

if __name__ == '__main__':
    #with open('./example.txt', 'r') as infile:
    with open('./input.txt', 'r') as infile:
        solve_pt1(infile)
        infile.seek(0)
        solve_pt2(infile)