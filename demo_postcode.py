#! /use/bin/env python3


import sys
# New code

import re
infile = open(r"C:\Users\Kohno\project\Python_Labs_Nov26\Python_Labs_Nov26\labs\postcodes.txt", 'r')
valid = 0
for postcode in infile:

    if postcode.isspace():continue

    postcode = postcode.upper()

    postcode = re.sub(r'\s+', r'', postcode)
    postcode = re. sub(r'(\d[A-Z](2))$', r'\1', postcode)

    m = re.search(r'^[A-Z](1,2)\d(1,2)[A-Z]?'\s\d[A-Z]{2}$, postcode)

    if m:
        valid += 1 
        print(postcode)
    else:
        invalid +=1


    print(postcode)

print(valid)


infile.close()