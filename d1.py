import common
import re

def d1(filename,puzzle):
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

    lines = common.read_lines(filename)
    for line in lines:
        if puzzle == 2:
            for a, b in subs:
                line = re.sub(a, b, line)
        number_array = re.findall(r'\d', line)
        number_string = number_array[0]+number_array[-1]
        final_array.append(int(number_string))


    total = 0
    for i in final_array:
        total = total+i

    print("Puzzle %s: %s" %(puzzle,total))
