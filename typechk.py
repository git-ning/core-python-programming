#!/usr/bin/python
#_*_coding:utf-8_*_

def dispayNumType(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!'

dispayNumType(-69)
dispayNumType(9999999999999999999999L)
dispayNumType(98.6)
dispayNumType(-5.2+1.9j)
dispayNumType('xxx')