#!/usr/bin/python

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

read = open("input2","r")

vowelstr = "aeiou"
vowels = {}
for ch in vowelstr:
    vowels[ch] = 1 
for line in read:
    line.rstrip() # get rid of newline
    vowelct = 0
    for ch in line:
        if vowels[ch]:
            vowelct += 1
    if vowelct >= 3:
        print line, "vowels ok"
