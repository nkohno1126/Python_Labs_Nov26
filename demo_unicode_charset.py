#! /use/bin/env python3

# Descripition 

import sys
# New code

for pos in range(0,65536):
    try:
        print(chr(pos), end=" ")
        if pos % 16 ==0:
            print()
    except UnicodeEncodeError:
        print('')


sys.exit(0)