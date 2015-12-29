#!/usr/bin/python
import re

measurepat = re.compile("(\S+) can fly (\d+) \S+ for (\d+) seconds, .+ (\d+) seconds")

def race(reindeer,time):
    state = 'run'
    distances = {}
    states = {}
    points = {}
    for r in reindeer.keys():
        distances[r] = 0
        points[r] = 0
        states[r] = { 'state' : 'run',
                      'run'   : 0,
                      'rest'  : 0 }

    for sec in range(time):
        for r in reindeer:
            state = states[r]
            stats = reindeer[r]

            if state['state'] == 'run':
                distances[r] += stats['speed']
                state['run'] += 1
                
                if state['run'] >= stats['stamina']:
                    state['state'] = 'rest'
                    state['run'] = 0
                
            elif state['state'] == 'rest':
                state['rest'] += 1
                if state['rest'] >= stats['restup']:
                    state['state'] = 'run'
                    state['rest'] = 0
            state[r] = state

        max_distance = max(distances.values())
        for d in sorted(distances,key=distances.get,reverse=True):
            if distances[d] < max_distance:
                break
            points[d] += 1
            
            
    return (distances,points)
        

TOTAL_TIME = 2503
f = open("input","rb")

reindeer = {}
for line in f:
    line = line.rstrip()
    m = measurepat.match(line)
    if m:
        #print m.group(1), m.group(2), m.group(3), m.group(4)
        reindeer[m.group(1)] = { "speed":   int(m.group(2)),
                                 "stamina": int(m.group(3)),
                                 "restup":  int(m.group(4)) }
    else:
        print "no match for ",line

(run_distances,pts) = race(reindeer, TOTAL_TIME)
for r in sorted(run_distances,key=run_distances.get,reverse=True):
    print r,pts[r],run_distances[r]

                  
#
#for rd in sorted(results,key=results.get,reverse=True):
#    print rd,results[rd]
