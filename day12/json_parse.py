#!/usr/bin/python
import re
import json

def check_sum(obj):
    in_sum = 0
 #   print "type is ",type(obj).__name__, " for ", obj
    if type(obj).__name__ == 'int':
        in_sum = obj
    elif type(obj).__name__ == 'list':
        for n in obj:
            in_sum += check_sum(n)
    elif type(obj).__name__ == 'dict':
        for k in obj.keys():
            #print " --> key is ",k, "val is ",obj[k]
            in_sum += check_sum(obj[k])
    return in_sum

def check_sum_nored(obj):
    in_sum = 0

    print "type is ",type(obj).__name__, " for ", obj
    if type(obj).__name__ == 'int':
        in_sum = obj
    elif type(obj).__name__ == 'list':
        for n in obj:
            in_sum += check_sum_nored(n)
    elif type(obj).__name__ == 'dict':
        addup = 0
        for k in obj.keys():
            print " --> key is ",k, "val is ",obj[k]
            if k == "red" or obj[k] == "red":
                addup = 0
                break
            
            addup += check_sum_nored(obj[k])
        in_sum += addup
    return in_sum

f = open("input","rb")

numfind = re.compile(r"(\-?\d+)")

for line in f:
    sum = 0
    line = line.rstrip()
    if line[0] == "#":
        continue
    for m in numfind.finditer(line):
        sum += int(m.group(1))
    obj = json.loads(line)
    comp_sum = check_sum(obj)
    nored_comp_sum = check_sum_nored(obj)
    print line
    print "--> sum is ",sum
    print "recursive comp sum is ", comp_sum
    print "recursive comp sum no red is ", nored_comp_sum
    print "---"
