#!/usr/bin/python
import re
import numpy

readfile = open("input","r")

counts = [ 0, 0]
for line in readfile:
    line = line.rstrip()
    nline = re.sub(r'\\',r'\\\\',line)
    sline = re.sub('\"','\\"',nline)
    sline = '"'+sline+'"'
    print line, sline,len(sline)
#    print len(line), len(n)
    counts[0] += len(line)
    counts[1] += len(sline)

print "totals are ", counts[0], counts[1]
print "final matchsticks answer:",counts[1] - counts[0]
