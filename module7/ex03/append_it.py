#!/usr/bin/env python3

import sys

if len(sys.argv)>1:
    i=1
    while i<len(sys.argv): 
        if sys.argv[i].find('ism')==-1:
            print(sys.argv[i]+'ism')
            i+=1
        else:
            i+=1
else:
    print('none')
