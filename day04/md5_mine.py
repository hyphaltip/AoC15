#!/usr/bin/python
import hashlib


mykey = "ckczppom"
#mykey = "abcdef"
# first part
leadingexpect = '00000'
# change to this for 2nd part
#leadingexpect = '000000'
leadingct = len(leadingexpect)
count = 1
found = 0
while found == 0:
    h = hashlib.new('md5')
    key = mykey + str(count)
    h.update(key)
    digest = h.hexdigest()
    print count, digest
    if digest[0:leadingct] == leadingexpect:
        print "found ",digest, key
        found = 1
    else:
        count += 1
