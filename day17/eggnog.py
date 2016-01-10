#!/usr/bin/python
import itertools

total_volume = 150
sizes = []
input = open("input",'rb')
# properties
for line in input:
    sizes.append(int(line))

count = 0
for n in range(2,len(sizes)):
    for p in itertools.combinations(sizes,n):
        if sum(p) == total_volume:
            count += 1

print "combinations to equal",total_volume, "is",count

count = 0
# just hard coding this, would be easy to determine it programatically though
smallest_size = 4;
for p in itertools.combinations(sizes,smallest_size):
    if sum(p) == total_volume:
        count += 1


print "number of combos of containers of %d is %d"%(smallest_size,count)
