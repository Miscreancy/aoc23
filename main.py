#! /usr/bin/env python3
import argparse
from d1 import d1
from d2 import d2
from d3 import d3
from d4 import d4

def parse_args():
    parser = argparse.ArgumentParser(
            prog="AoCD2",
            description="Solver for Advent pf Code 2023 Day 2",
            )
    parser.add_argument('-f','--filename',dest="filename",required=True,help="filename of the input file for day 2")
    parser.add_argument('-p','--puzzle',dest="puzzle",choices=["d1","d2","d3","d4"],required=True,help="Which day's puzzle to solve")
    parser.add_argument('-n','--number',dest="number",choices=[1,2],required=True,help="Which of the selected day's puzzles to solve: 1 or 2",type=int)
    args = parser.parse_args()
    return args

def call_function(puzzle,filename,number):
    puzzle_dict = {
        "d1": d1,
        "d2": d2,
        "d3": d3,
        "d4": d4
        }
    puzzle_dict[puzzle](filename,number)


def main():
    args=parse_args()
    filename = args.filename
    puzzle = args.puzzle
    number= args.number
    call_function(puzzle,filename,number)


if __name__ == '__main__':
    main()
