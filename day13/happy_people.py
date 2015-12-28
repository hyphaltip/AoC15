#!/usr/bin/python
import re
import itertools

def score_iter(order,scoretable):
    s = 0
    # intentionally asking of -1 as well here e.g(0 - 1)
    # to get the last of the list paired with the first
    for i in range(len(order)):
        p1 = order[i-1] + "," + order[i]
        p2 = order[i] + "," + order[i-1]
    #    print p1,"<=>",p2
        s += scoretable[p1] + scoretable[p2]
    #print "s is ",s
    return s

f = open("input","rb")

lineparse = re.compile("(\S+) would (gain|lose) (\d+) .+ next to (\S+)\.")
happyscore = {}
people = {}
for line in f:

    m = lineparse.match(line)
    if m:
#        print m.group(1), m.group(2), m.group(3), m.group(4)
        points = int( m.group(3))
        if m.group(2) == "lose":
            points *= -1
        people[m.group(1)] = 1
        people[m.group(4)] = 1
        pair = m.group(1) + "," + m.group(4)
        happyscore[pair] = points


guests = people.keys()
best_score = 0
best_arrangement = []
for iter in itertools.permutations(guests):
    score = score_iter(iter,happyscore)
#    print 'score is ', score
    if score >= best_score:
        best_score = score
        best_arrangement = iter


print "best score is ", best_score
print "best arrangement is", best_arrangement

for p in guests:
    p1 = "Self"+','+p
    p2 = p+","+"Self"

    happyscore[p1] = 0
    happyscore[p2] = 0

people["Self"] = 1
guests = people.keys()

best_score = 0
best_arrangement = []
for iter in itertools.permutations(guests):
    score = score_iter(iter,happyscore)
    if score >= best_score:
        best_score = score
        best_arrangement = iter

print "---"
print "Now with 'Self' added in"
print "best score is ", best_score
print "best arrangement is", best_arrangement
