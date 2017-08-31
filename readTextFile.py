#!/usr/bin/python
#_*_coding:utf-8_*_

"""readTextFile.py -- read and display text file"""

# get file name
fname = raw_input('Enter filename:')
print

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print "***File open ERROR:***", e
else:
    for eachline in fobj:
        print eachline
    fobj.close()