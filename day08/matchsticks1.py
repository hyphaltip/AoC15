#!/usr/bin/python
import re
import numpy

readfile = open("input","r")

counts = [ 0, 0]
for line in readfile:
    line = line.rstrip()
    n = eval(line)
    print len(line), len(n)
    counts[0] += len(line)
    counts[1] += len(n)

print "totals are ", counts[0], counts[1]
print "final matchsticks answer:",counts[0] - counts[1]
