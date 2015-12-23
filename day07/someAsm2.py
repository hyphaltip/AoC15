#!/usr/bin/python
import re
import numpy
import copy

pyoperators = { "AND":'%d & %d',
                "OR" : '%d | %d',
                'LSHIFT' : '%d << %d',
                'RSHIFT' : '%d >> %d' }
MAX=2**16-1
fin = re.compile(r"(.+)\s+\-\>\s+(\S+)")

def circuit(tempwires):
    asnpat = re.compile(r"^(\S+)$")
    notpat = re.compile(r"NOT\s+(\S+)")
    combpat = re.compile(r"(\S+)\s+(AND|OR|LSHIFT|RSHIFT)\s+(\S+)")

    wires = {}
    incomplete = tempwires.keys()    
    while len(incomplete) > 0:
        #print incomplete, "entries in tempwires"
        for wire in incomplete:
            logic = tempwires[wire]
            print "logic is ",logic, " for ",wire
            # asnpat
            m = asnpat.match(logic)
            if m:
                if m.group(1).isalpha():
                    if m.group(1) in wires:
                        wires[wire] = wires[m.group(1)]
                        tempwires.pop(wire)
                else:
                    wires[wire] = int(m.group(1))
                    tempwires.pop(wire)
                continue
        
            # not pattern
            m = notpat.match(logic)
            if m:
                if m.group(1).isalpha():
                    #print "match is ",m.group(0)
                    if m.group(1) in wires:
                        wires[wire] = (MAX - wires[m.group(1)])
                        tempwires.pop(wire)

                else:
                    wires[wire] = m.group(1)
                    tempwires.pop(wire)
                continue
        

            # operators
            m = combpat.match(logic)
            if m:
                #print "match was ", m.group(0), " for ", wire
                lopt = m.group(1)
                if lopt.isalpha():
                    if lopt in wires:
                        lopt = wires[lopt]
                    else:
                        #print "lopt is",lopt, " not defined yet"
                        continue
                else:
                    lopt = int(lopt)
            
                ropt = m.group(3)
                if ropt.isalpha():
                    if ropt in wires:
                        ropt = wires[ropt]
                    else:
                        #print "ropt is",ropt,"not defined yet"
                        continue
                else:
                    ropt = int(ropt)
        
                expr = pyoperators[m.group(2)] % (lopt,ropt)
                #print "expr is ",expr
                val = eval(expr)
                wires[wire] = val
                tempwires.pop(wire)
                continue
            else:
                print "logic ", logic, " didn't match"
            
        incomplete = tempwires.keys()
    return wires

cmds = {}

readfile = open("input","r")

for line in readfile:
    m = fin.match(line)
    if m:
        cmds[m.group(2) ] = m.group(1)        
    else:
        print "unexpected logic in ",line

cmdscopy = copy.deepcopy(cmds)
finalwires = circuit(cmds)

wirenames = finalwires.keys()
wirenames.sort()
#for wire in wirenames:
#    print wire, finalwires[wire]


print "a = ",finalwires["a"]
cmdscopy["b"] = str(finalwires["a"])
finalwires = circuit(cmdscopy)

print " second run value of a is ", finalwires["a"]




