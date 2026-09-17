#!/usr/bin/env python3

import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    while len(text)<8:
        text += 'Z'
    print(text)

if len(sys.argv)>1:

    i=1
    while i<len(sys.argv):
        if len(sys.argv[i])>8:
            shrink(sys.argv[i])
        elif len(sys.argv[i])==8:
            print(sys.argv[i])
        else:
            enlarge(sys.argv[i])

        i+=1
else:
    print('none')
