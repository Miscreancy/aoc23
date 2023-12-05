import common
import re

def d4(filename,puzzle):
    lines = common.read_lines(filename)

    points = 0
    indexRepeats = {}
    totalRepeats = 0
    cards = len(lines)
    for i in range(cards):
        indexRepeats[i]=1

    for index,line in enumerate(lines):
        repeats=indexRepeats[index]
        totalRepeats+=repeats
        cardPoints=0
        winners = line.split(':')[1].split("|")[0].split()
        numbers = line.split(':')[1].split("|")[1].split()
        matches = len([i for i in numbers if i in winners])
        if matches > 0:
            for i in range(index+1,index+matches+1):
                newRepeats = indexRepeats[i] + repeats
                indexRepeats[i] = newRepeats
            for i in range(matches):
                if cardPoints == 0:
                    cardPoints+=1
                else:
                    cardPoints+=cardPoints
        points+=cardPoints

    if puzzle == 1:
        print("Puzzle 1: ",points)
    else:
        print("Puzzle 2: ",totalRepeats)
