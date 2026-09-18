#!/usr/bin/env python3

import sys

def shrink(word):
    return(word[:8])

def enlarge(word):
    while len(word)<8:
        word = word + 'Z'
    return(word)

if len(sys.argv)<2:
    print('none')
else:
    i=1
    while i<len(sys.argv):
        if len(sys.argv[i])<8:
            print(enlarge(sys.argv[i]))
        elif len(sys.argv[i])>8:
            print(shrink(sys.argv[i]))
        else:
            print(sys.argv[i])
        i+=1
