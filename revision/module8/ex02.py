#!/usr/bin/env python3

import sys

def downcase_all():
    if len(sys.argv)<2:
        print('None')
    else:
        i = 1
        while i<len(sys.argv):
            print(sys.argv[i].lower())
            i+=1

downcase_all()
