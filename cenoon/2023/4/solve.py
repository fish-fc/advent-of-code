#!/usr/bin/python
import math

def solve_pt1(infile):
    total = 0
    for line in infile:
        # parse out number lists from input
        parse_num_list = line.split(':')[1].split('|')
        winning_nums = parse_num_list[0].strip().split()
        scratch_nums = parse_num_list[1].strip().split()

        # use powers of 2 to double for every match
        # 2 ^ -1 == 0.5, the floor will give 0 if no matches
        winning_amt = -1
        for num in scratch_nums:
            if num in winning_nums:
                winning_amt += 1
        total += math.floor(pow(2, winning_amt))
    print(total)

def solve_pt2(infile):
    total = 0
    # have to populate card list based on number of lines/cards
    num_cards = []
    for i in enumerate(infile):
        num_cards.append(1)
    infile.seek(0)
    
    for i, line in enumerate(infile):
        # parse out number lists from input
        parse_num_list = line.split(':')[1].split('|')
        ref_nums = parse_num_list[0].strip().split()
        scratch_nums = parse_num_list[1].strip().split() 
        
        # increment the number of cards in the list based on matches
        match_amt = 0
        for num in scratch_nums:
            if num in ref_nums:
                match_amt += 1
        # add the match amount to num_cards list * amount of cards currently in list
        for y in range(0, num_cards[i]):
            for x in range(0, match_amt):
                num_cards[i+x+1] += 1

    print(sum(num_cards))

if __name__ == '__main__':
    #with open('./example.txt', 'r') as infile:
    with open('./input.txt', 'r') as infile:
        solve_pt1(infile)
        infile.seek(0)
        solve_pt2(infile)