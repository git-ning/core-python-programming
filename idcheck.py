#!/usr/bin/python
#_*_coding:utf-8_*_

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Tdentifier to test:\n')

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print '''invalid: first symbol must be alphabetic'''
    else:
        alphnums = alphas + nums
        for otherChar in myInput[1:]:
            if otherChar not in alphnums:
                print '''invalid: remaining
                symbols must be alphanumeric'''
                break
            else:
                print "okay as an identifier"