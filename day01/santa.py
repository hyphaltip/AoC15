#import urllib2
#url='http://adventofcode.com/day/1/input'
#instructions = urllib2.urlopen(url)
file="input"
instructions = open(file,'rb')
floor=0

counter = 0
for dir in instructions:
    for ch in dir:
        counter += 1
        if ch == "(":
            floor += 1
        elif ch == ")":
            floor -= 1
            
        if floor == -1:
            print "floor for ",floor, " is ", counter

print "final floor is",floor
            
