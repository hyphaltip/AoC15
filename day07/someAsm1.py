#!/usr/bin/python
import re
import numpy

pyoperators = { "AND":'%d & %d',
                "OR" : '%d | %d',
                'LSHIFT' : '%d << %d',
                'RSHIFT' : '%d >> %d' }
MAX=2**16-1
wires = {}
tempwires = {}
asnpat = re.compile(r"^(\S+)$")
notpat = re.compile(r"NOT\s+(\S+)")
combpat = re.compile(r"(\S+)\s+(AND|OR|LSHIFT|RSHIFT)\s+(\S+)")
fin = re.compile(r"(.+)\s+\-\>\s+(\S+)")

readfile = open("input","r")

for line in readfile:
    m = fin.match(line)
    if m:
        print "match are",m.group(1),m.group(2)
        n = asnpat.match(m.group(1))
        if n and (not n.group(1).isalpha()):
            # simple assignment of numeric here
            wires[m.group(2)] = int(m.group(1))
        else:
            tempwires[m.group(2)] = m.group(1)

            
incomplete = tempwires.keys()
while len(incomplete) > 0:
    print incomplete, "entries in tempwires"
    for wire in incomplete:
        logic = tempwires[wire]

        # asnpat

        m = asnpat.match(logic)
        if m:
            if m.group(1) in wires:
                wires[wire] = wires[m.group(1)]
                tempwires.pop(wire)
                continue
        
        # not pattern
        m = notpat.match(logic)
        if m:
            print "match is ",m.group(0)
            if m.group(1) in wires:
                wires[wire] = (MAX - wires[m.group(1)])
                tempwires.pop(wire)
                continue
        

        # operators
        m = combpat.match(logic)
        if m:
            print "match was ", m.group(0), " for ", wire
            lopt = m.group(1)
            if lopt.isalpha():
                if lopt in wires:
                    lopt = wires[lopt]
                else:
                    print "lopt is",lopt, " not defined yet"
                    continue
            else:
                lopt = int(lopt)
            
            ropt = m.group(3)
            if ropt.isalpha():
                if ropt in wires:
                    ropt = wires[ropt]
                else:
                    print "ropt is",ropt,"not defined yet"
                    continue
            else:
                ropt = int(ropt)
        
            expr = pyoperators[m.group(2)] % (lopt,ropt)
            print "expr is ",expr
            val = eval(expr)
            wires[wire] = val
            tempwires.pop(wire)
            continue
        else:
            print "logic ", logic, " didn't match"
            
    incomplete = tempwires.keys()
    
wirenames = wires.keys()
wirenames.sort()
for wire in wirenames:
    print wire, wires[wire]
