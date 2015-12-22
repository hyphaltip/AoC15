#!/usr/bin/python
import re
import numpy
readfile = open("input","r")

height = 1000
width  = 1000
matrix = numpy.zeros((height, width))


parse = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")

for line in readfile:
    m = parse.match(line)
    startx=starty=endx=endy=0
    command = ""
    if m:
        command=m.group(1)
        startx = int(m.group(2))
        starty = int(m.group(3))
        endx   = int(m.group(4))
        endy   = int(m.group(5))
    else:
        print "no parse match for line:",line

    print command,startx,starty,"-",endx,endy
    val = 0
    if command == "turn on":
        val = 1
    elif command == "turn off":
        val = -1
    elif command == "toggle":
        val = 2
    else:
        print "unknown command: ",command
       
    for x in range(startx,endx+1,1):
        for y in range(starty,endy+1,1):
            matrix[x][y] += val
            if matrix[x][y] < 0:
                matrix[x][y] = 0
total = 0
print sum(matrix)
for row in matrix:
    total += sum(row)
print "total light =",int(total)
