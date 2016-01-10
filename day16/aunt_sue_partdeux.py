#!/usr/bin/python
import re
import itertools



known = {}
input = open("properties",'rb')
# properties
for line in input:
    kv = line.split(": ")
    known[kv[0]] = int(kv[1])

print "known is ", known
pat = re.compile("Sue (\d+):\s+(.+)")
input = open("input",'rb')

# sues
for line in input:
    m = pat.match(line)
    if m:
        sueid = int(m.group(1))
        quals = m.group(2).split(", ")
        positives = 0
        negatives = 0
        for qual in quals:
            kv = qual.split(": ")
            kv[1] = int(kv[1])
            #print "comparing [%d] = %s"%(sueid,kv)

            if kv[0] == "cats" or kv[0] == "trees":
                if kv[1] > known[kv[0]]:
                    # print "%d known [%s] = %d vs %d " %( sueid, kv[0], known[kv[0]],kv[1])
                    positives += 1
                else:
                    negatives += 1
            elif kv[0] == "pomeranians" or kv[0] == "goldfish":
                if kv[1] < known[kv[0]]:
                    # print "%d known [%s] = %d vs %d " %( sueid, kv[0], known[kv[0]],kv[1])
                    positives += 1
                else:
                    negatives += 1
            else:
                if kv[1] == known[kv[0]]:
                    # print "%d known [%s] = %d vs %d " %( sueid, kv[0], known[kv[0]],kv[1])
                    positives += 1
                else:
                    negatives += 1
                    
        if( negatives == 0 ):
            print sueid, "consistent"

    else:
        print "no match for ",line
