#!/usr/bin/python
#_*_coding:utf-8_*_

"""makeTextFile.py -- create text file"""

import os

ls = os.linesep
fname = 'test.txt'

# get file name
while True:

    if os.path.exists(fname):
        print "ERROR: '%s already exists" % fname
    else:
        break

# get file content (text) line
all = []
print "\nEnter lines('.' by itself to quit).\n"

# loop until user terminates input
while True:
    entery = raw_input('>')
    if entery == '.':
        break
    else:
        all.append(entery)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'DONE!'
