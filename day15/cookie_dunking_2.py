#!/usr/bin/python
import re
import itertools

#def add_group(others):
#    sums = []
#    if( n > len(others)):
#        return
#    elif others[n]
#        sums.append()       
   # do all combos of the lists
#    
#    return sums


pat = re.compile("(\S+):\s+(.+)")
input = open("input2",'rb')

ingredients = {}
ingredientsorder = []
for line in input:
    p = line.split(":")
    ingredients[p[0]] = {}
    ingredientsorder.append(p[0])
    props = p[1].lstrip().rstrip().split(", ")
    for prop in props:
        t = prop.split(" ")
        c = ingredients[p[0]]
        c[t[0]] = int(t[1])

# enumerate proportions that will sum to 100
total = 0
MAX = 100
measurements = {}

matching_sums = []
for i in ingredients:
    measurements[i] = range(44,MAX)
    #print measurements[i]


    
bestscore = 1
bestcombo = []
for i in measurements:
    iorder = 0
    for n in measurements[i]:
        cookie_n = ingredients[ ingredientsorder[iorder] ]
        for m in measurements[i]:
            if (m + n) > MAX:
                break
            cookie_m = ingredients[ ingredientsorder[iorder+1] ]
            if n+m == MAX:
                totscore = 1
                print n,m
                for prop in cookie_n:
                    if prop == "calories":
                        continue
                    
                    propscore = n*cookie_n[prop] + m*cookie_m[prop]
                    if propscore < 0:
                        propscore = 0
                        
                    print "prop is ",prop, " score is ", propscore
                    totscore *= propscore
                    print "totscore is",totscore
                    if totscore > bestscore:
                        bestscore = totscore
                        bestcombo = [n,m]
                        

# this is the brute force longest way to do this

for i in ingredients:
    for prop in ingredients[i]:        
        print i,prop,ingredients[i].get(prop)

print "bestscore is ",bestscore, "combo is ",bestcombo

