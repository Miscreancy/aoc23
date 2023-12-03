#! /usr/bin/env python3
import re
import argparse

parser = argparse.ArgumentParser(
        prog="AoCD2",
        description="Solver for Advent pf Code 2023 Day 2",
        )
parser.add_argument('-f','--filename',dest="filename",required=True,help="filename of the input file for day 2")
parser.add_argument('-p','--puzzle',dest="puzzle",choices=[1,2],required=True,help="Which of the day's puzzles to solve: 1 or 2",type=int)
args = parser.parse_args()

inputfile = open(args.filename, "r")
puzzle = args.puzzle

final_array=[]

limit_dict = {
        "red": 12,
        "blue": 14,
        "green": 13
        }

lines = inputfile.readlines()
for line in lines:
    game_pass = True
    value_dict = {
        "blue": 0,
        "red": 0,
        "green": 0
    }
    linearray = line.split(':')
    game_id = linearray[0].split()[1]
    games = linearray[1].split(";")
    for game in games:
        stages = game.split(',')
        for stage in stages:
            number = int(stage.split()[0])
            colour = stage.split()[1]
            if puzzle == 1:
                if number > limit_dict[colour]:
                    game_pass = False
            else:
                if number > value_dict[colour]:
                    value_dict.update({colour:number})
    if puzzle == 1:
        if game_pass:
            final_array.append(int(game_id))
    else:
        power = int(value_dict["red"] * value_dict["blue"] * value_dict["green"])
        final_array.append(power)

inputfile.close()

total = 0
for i in final_array:
    total = total+i
print(total)
