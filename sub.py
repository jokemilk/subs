#!/usr/bin/env python

#print 'hello world'

f=open('test.c')

for i in f:
    if 'PRINT' in i:
        l=i.split('"')
        for j in xrange(1,len(l) - 1):
            if 'PRINT' in l[j-1]:
                l[j] = '"hacked"'
        print ''.join(l),
    else:
        print i,
