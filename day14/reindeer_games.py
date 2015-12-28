#!/usr/bin/python
import re

measurepat = re.compile("(\S+) can fly (\d+) \S+ for (\d+) seconds, .+ (\d+) seconds")

def race(speed,stamina,restup,time):
    state = 'run'
    distance = 0
    cur_run = 0
    cur_rest = 0
    for sec in range(time):
        if state == 'run':
            distance += speed
            cur_run += 1
            if cur_run >= stamina:
                state = 'rest'
                cur_run = 0

        elif state == 'rest':
            cur_rest += 1
            if cur_rest >= restup:
                state = 'run'
                cur_rest = 0
    return distance
        

TOTAL_TIME = 2503
f = open("input","rb")

reindeer = {}
results = {}
for line in f:
    line = line.rstrip()
    m = measurepat.match(line)
    if m:
        #print m.group(1), m.group(2), m.group(3), m.group(4)
        results[m.group(1)] = race(int(m.group(2)),
                                   int(m.group(3)),
                                   int(m.group(4)),
                                   TOTAL_TIME)
        reindeer[m.group(1)] = { "speed": int(m.group(2)),
                                 "stamina": int(m.group(3)),
                                 "resttime": int(m.group(4)) }
    else:
        print "no match for ",line


                  

for rd in sorted(results,key=results.get,reverse=True):
    print rd,results[rd]
