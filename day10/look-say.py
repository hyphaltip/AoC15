#!/usr/bin/python

input = 1
input = 3113322113
steps = 50 #part 2 asks for 50 instead of 40

def look_say(msg):
    # need to compress this string first
    msg = str(msg)
    #print "msg is: ",msg
    runs = []
    run = 1
    lastch = msg[0]
    msg = msg[1:]
    for ch in msg:
        if lastch == ch:
            run += 1
        else:
            runs.append(str(run)+str(lastch))
            run = 1
        lastch = ch
    runs.append(str(run)+str(lastch))
    return "".join(runs)

m = input
print m
for n in range(steps):
    m = look_say(m)
#    print m, len(m)
    print len(m)
