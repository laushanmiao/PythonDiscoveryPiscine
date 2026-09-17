#!/usr/bin/env python3

import sys

def downcase_it():
    if len(sys.argv)>1:
        i=1
        while i < len(sys.argv):
            print(str(sys.argv[i]).lower())
            i+=1
    else:
        print('none')

downcase_it()
