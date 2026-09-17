#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 3:
    no = len(re.findall(sys.argv[1], sys.argv[2]))
    if no !=0:
        print(no)
    else:
        print('none')
else:
    print('none')
