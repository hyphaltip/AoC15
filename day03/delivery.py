#!/usr/bin/python

input = open("input","r")

move = { ">" : [1,0],
         "<" : [-1,0],
         "^" : [0,1],
         "v" : [0,-1] }

for line in input:
    line = line.rstrip()
    x=0
    y=0
    xr = 0
    yr = 0
    coord = [str(x),str(y)]
    presents = [ ",".join(coord) ]
    presents.append( ",".join(coord))
    turn = 0
    for direction in line:
        offset = move[direction]
        coord = []
        if turn == 0:
            x += offset[0]
            y += offset[1]
            coord = [ str(x),str(y)]
        else:
            xr += offset[0]
            yr += offset[1]        
            coord = [ str(xr),str(yr)]

        presents.append(",".join(coord) )
        turn = 1 - turn
    presents.sort()
    unique = set(presents)
    print "houses: ",len(unique)
