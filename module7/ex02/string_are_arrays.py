#!/usr/bin/env python3

import sys
import re

if len(sys.argv)>1:
    zs = len(re.findall(r'z', sys.argv[1]))
    if zs >=1:
        for item in (re.findall(r'z', sys.argv[1])):
            print(item,end='')
        print()
    else:
        print('none')
else:
    print('none')
