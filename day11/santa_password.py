#!/usr/bin/python
import re

def increment(msg):
    
    carry = 1
    newpass=[]
    for c in reversed(msg):
        if carry:
            c=chr(ord(c)+1)
            carry = 0
        if c == "{":
            c = "a"
            carry = 1
            
        newpass.append(c)

    return "".join(newpass[::-1])

def hasStraight(msg):
    
    for n in range(len(msg)-3):
        #print "n is ",n,"section is ",msg[n:n+3]
        
        l = ord(msg[n])
        status = True
        for ch in msg[n+1:n+3]:
           # print "ch is ",ch, ord(ch),"l is ",l
            if( ord(ch) != (l + 1)):
                status = False
                continue
            l = ord(ch)
        if status:
            return True
    return False

ambpat = re.compile(r"[iol]")
def hasAmbiguity(msg):
    return ambpat.search(msg)

pairpat = re.compile(r"([a-z])\1")
def hasMultiplePairs(msg):
    pairs = {}
    lastch = ""
    n = 0
    for ch in msg:
        if n > 0 and lastch == ch:
            pairs[lastch] = n
        n += 1
        lastch = ch
    if len(pairs.keys()) > 1:
        return True
    return False

# my key
p = "vzbxkghb"

print "in:",p
while not hasStraight(p) or hasAmbiguity(p) or not hasMultiplePairs(p):
    p = increment(p)
#    print "out:",p
    
print "good password ", p

# part 2
p = increment(p)
while not hasStraight(p) or hasAmbiguity(p) or not hasMultiplePairs(p):
    p = increment(p)
    
print "good password ", p
