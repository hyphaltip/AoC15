#!/usr/bin/python
import re
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

read = open("input","r")

vowelpattern = re.compile("[aeiou]")
rpat  = re.compile(r"([a-z])\1")
naughty = re.compile('ab|cd|pq|xy')

nice_count = 0
for line in read:
    line = line.rstrip() # get rid of newline
    if naughty.search(line):
  #      print "line",line, "is naughty by pattern"
        continue
   # print "line is ",line
    vowels = vowelpattern.findall(line)
    #print "vowels are ",str(vowels)
    m = rpat.search(line)

#    if m:
#        print "match group is ", m.group(1)

    if len(vowels) >= 3 and m:
#       print line, "vowels ok; letter_run is"
       nice_count += 1

print "nice count is",nice_count
