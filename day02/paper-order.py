#!/usr/bin/python

allpaper =0
allribbon=0
input=open("input",'r')
for line in input:
    line = line.rstrip()
    dim = line.split('x')
    print "dim is ",dim
    l= int(dim[0])
    w= int(dim[1])
    h= int(dim[2])
#    print "l=%d,w=%d,h=%d" % (l,w,h)
    sa = (2*l*w, 2*w*h, 2*h*l)
    sides = (l*w,l*h,w*h)
#    print "sa", sum(sa)
#    print "sides are",sides
    total = sum(sa) + min(sides)
#    print "total is",total
    allpaper += total
# ribbon
    sidesort = [l,w,h]
    sidesort.sort()
    ribbon  = 2*sidesort[0] + 2*sidesort[1]
    bow = l*w*h
    print "ribbon:",ribbon,"bow:",bow, " total of ",ribbon+bow
    allribbon += bow + ribbon


print "total paper needed:",allpaper
print "total ribbon needed:",allribbon

