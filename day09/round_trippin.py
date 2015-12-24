#!/usr/bin/python
import re
import itertools


readfile = open("input","r")

pat = re.compile(r"(\S+)\s+to\s+(\S+)\s+=\s+(\d+)")
cities = {}
distance = {}
for line in readfile:
    line = line.rstrip()
    m = pat.match(line)
    if m:
        cfrom = m.group(1)
        cto   = m.group(2)
        cdist = m.group(3)
        cities[cfrom] = 1
        cities[cto]   = 1
        n = [cfrom,cto]
        distance[",".join(n)] = int(cdist)
        n = [cto,cfrom]
        distance[",".join(n)] = int(cdist)
    else:
        print "line unmatched:",line

citylist = set(cities.keys())
print "citylist is ",citylist

# this is slightly stupid, all combos - should be able to
# to cut this in half if the computation is too 
trips = {}
for iter in itertools.permutations(citylist):
    #print iter
    key = " -> ".join(iter)
    lastcity = ""
    total_distance = 0
    for city in iter:
        if lastcity:
            d = distance[",".join([lastcity,city])]
            #print "%s->%s %d" % (lastcity,city,d)
            total_distance += d
        lastcity = city
    #print "%s = %d" % (key, total_distance)
    trips[key] = total_distance

for trip in sorted(trips,key=trips.get,reverse=True):
    print "%s = %d" % (trip,trips[trip])
