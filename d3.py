import common
import re

'''
I've refactored my bash code but left my original python implementation; the original bash was similar.

Messy as heck, done in 90 minutes at 5am while half asleep, but I own my own quick solutions.
'''

def d3(filename,puzzle):
    if puzzle == 1:
        puzzle_1(filename,puzzle)
    else:
        puzzle_2(filename,puzzle)


def puzzle_1(filename,puzzle):
    final_array=[]
    discount_array=[]
    lines = common.read_lines(filename)
    maxheight=len(lines)-1
    maxwidth = len(lines[0])-1
    for index,line in enumerate(lines):
        for idx,item in enumerate(line):
            digit_array=[]
            if item.isdigit():
                match = False
                position=str(index)+","+str(idx)
                if position in discount_array:
                    continue
                vscounter=define_search_area(index,maxheight)
                hscounter=define_search_area(idx,maxwidth)
                for v in vscounter:
                    for h in hscounter:
                        search_position = str(v)+","+str(h)
                        if search_position == position:
                            continue
                        c=re.match(r'[^\d\.]',lines[v][h])
                        if c != None:
                            match = True
                if match == True:
                    back_array=[]
                    forw_array=[]
                    backi=idx-1
                    forwi=idx+1
                    while backi >= 0:
                        if line[backi].isdigit():
                            back_array.append(line[backi])
                            backi=backi-1
                        else:
                            backi=-1
                    if len(back_array) > 0:
                        for back in reversed(back_array):
                            digit_array.append(back)
                    digit_array.append(item)
                    while forwi <= maxwidth:
                        fitem=line[forwi]
                        if fitem.isdigit():
                            forw_array.append(line[forwi])
                            forw_position=str(index)+','+str(forwi)
                            discount_array.append(forw_position)
                            digit_array.append(fitem)
                            forwi=forwi+1
                        else:
                            forwi=maxwidth+1

                    digit = ''.join(digit_array)
                    final_array.append(int(digit))

    total = 0
    for i in final_array:
         total = total+i
    print("Puzzle %s: %s" %(puzzle,total))

def puzzle_2(filename,puzzle):
    final_array=[]
    discount_array=[]
    lines = common.read_lines(filename)
    maxheight=len(lines)-1
    for index,line in enumerate(lines):
        for idx,item in enumerate(line):
            maxwidth = len(lines[0])-1
            cog=re.match(r'\*',item)
            if cog != None:
                part_array=[]
                position=str(index)+','+str(idx)
                vscounter=define_search_area(index,maxheight)
                hscounter=define_search_area(idx,maxwidth)
                surrounding_array=[]
                for v in vscounter:
                    for h in hscounter:
                        digit_array=[]
                        search_position = str(v)+","+str(h)
                        if search_position in discount_array:
                            continue
                        char=lines[v][h]
                        surrounding_array.append(char)
                        if char.isdigit():

                            back_array=[]
                            forw_array=[]
                            backi=h-1
                            forwi=h+1
                            while backi >= 0:
                                if lines[v][backi].isdigit():
                                    back_array.append(lines[v][backi])
                                    backi=backi-1
                                else:
                                    backi=-1
                            if len(back_array) > 0:
                                for back in reversed(back_array):
                                    digit_array.append(back)
                            digit_array.append(char)
                            while forwi <= maxwidth:
                                fitem=lines[v][forwi]
                                if fitem.isdigit():
                                    forw_array.append(lines[v][forwi])
                                    forw_position=str(index)+','+str(forwi)
                                    discount_array.append(forw_position)
                                    digit_array.append(fitem)
                                    forwi=forwi+1
                                else:
                                    forwi=maxwidth+1

                            digit = ''.join(digit_array)
                            part_array.append(digit)
                dedup_part_array=list(set(part_array))
                if len(dedup_part_array) == 2:
                    ratio=int(dedup_part_array[0])*int(dedup_part_array[1])
                    final_array.append(ratio)
    total = 0
    for i in final_array:
         total = total+i
    print("Puzzle %s: %s" %(puzzle,total))

def define_search_area(index,max):
    if not index == 0 and not index == max:
        area=[index-1,index,index+1]
    elif index == 0:
        area=[index,index+1]
    else:
        area=[index-1,index]
    return area
