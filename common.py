def read_lines(filename):
    inputfile = open(filename, 'r')
    lines = inputfile.read().splitlines()
    inputfile.close()
    return lines
