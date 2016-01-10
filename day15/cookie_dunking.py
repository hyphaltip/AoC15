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
input = open("input",'rb')

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
    measurements[i] = range(1,MAX)
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
            for o in measurements[i]:
                if (m + n + o) > MAX:
                    break
                cookie_o = ingredients[ ingredientsorder[iorder+2] ]
                for p in measurements[i]:
                    if( n+m+o+p) > MAX:
                        break
                    cookie_p = ingredients[ ingredientsorder[iorder+3] ]
                    if n+m+o+p == MAX:
                        totscore = 1
                        #print n,m,o,p
                        prop = "calories"
                        calscore = n*cookie_n[prop] + m*cookie_m[prop] + o*cookie_o[prop] + p * cookie_p[prop]
# part 2                        
                        if calscore == 500:
# part 2 added
                            for prop in cookie_n:
                                if prop == "calories":
                                    continue
                                propscore = n*cookie_n[prop] + m*cookie_m[prop] + o*cookie_o[prop] + p * cookie_p[prop]
                                if propscore < 0:
                                    propscore = 0
                                print "prop is ",prop, " score is ", propscore
                                totscore *= propscore
                            print "totscore is",totscore
                            if totscore > bestscore:
                                bestscore = totscore
                                bestcombo = [n,m,o,p]
                        

# this is the brute force longest way to do this

for i in ingredients:
    for prop in ingredients[i]:        
        print i,prop,ingredients[i].get(prop)

print "bestscore is ",bestscore, "combo is ",bestcombo

