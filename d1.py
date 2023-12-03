#! /usr/bin/env python3
import re
import argparse

parser = argparse.ArgumentParser(
        prog="AoCD1",
        description="Solver for Advent of Code 2023 Day 1",
        )
parser.add_argument('-f','--filename',dest="filename",required=True,help="filename of the input file for day 1")
parser.add_argument('-p', '--puzzle',dest="puzzle",choices=[1,2],required=True,help="Which of the day's puzzles to solve: 1 or 2",type=int)
args = parser.parse_args()

inputfile = open(args.filename, "r")

final_array=[]
subs = [
    ('one','o1e'),
    ('two','t2o'),
    ('three','t3e'),
    ('four','4'),
    ('five','5e'),
    ('six','6'),
    ('seven','7n'),
    ('eight','e8t'),
    ('nine','n9e')
]

lines = inputfile.readlines()
for line in lines:
    if args.puzzle == 2: 
        for a, b in subs:
            line = re.sub(a, b, line)
    number_array = re.findall(r'\d', line)
    number_string = number_array[0]+number_array[-1]
    final_array.append(int(number_string))

inputfile.close()

total = 0
for i in final_array:
    total = total+i

print(total)
