#!/usr/bin/python
import re
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

read = open("input","r")

rpat  = re.compile(r"([a-z])([a-z]).*\1\2")
rpat2  = re.compile(r"([a-z])[a-z]\1")


nice_count = 0
for line in read:
    line = line.rstrip() # get rid of newline
    m = rpat.search(line)
    n = rpat2.search(line)
    if m and n:
        print line, "m:",m.group(0),m.group(1)+m.group(2)
        print "n:",n.group(0),n.group(1)
        nice_count += 1

print "nice count is",nice_count
