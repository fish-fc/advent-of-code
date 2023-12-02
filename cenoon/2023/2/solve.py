#!/usr/bin/python
def solve_pt1(infile):
    pass

def solve_pt2(infile):
    pass

if __name__ == '__main__':
    with open('./example.txt', 'r') as infile:
    #with open('./input.txt', 'r') as infile:
        solve_pt1(infile)
        infile.seek(0)
        solve_pt2(infile)