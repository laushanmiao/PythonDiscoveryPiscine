#!/usr/bin/env python3

import sys

def greetings():
    if len(sys.argv)<2:
        print('none')
    else:
        i=1
        while i<len(sys.argv):
            if sys.argv[i] == '':
                print('Hello, noble stranger.')
            elif isinstance(sys.argv[i], str)==False:
                print('Error! It was not a name. ')
            else:
                print('Hello, '+sys.argv[i]+'. '
                    )
            i+=1

greetings()
