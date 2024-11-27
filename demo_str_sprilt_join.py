#! /use/bin/env python3


import sys
# New code

line= r'root:x:0:0:The super User:/root:/bin:ksh'

fields = line.split(':') #returns a LIST which is MUTABLR
print(fields)
fields[4] = 'THe adminstration'
fields[6] = 'bin\bash'


line = ':'.join(fields)
print(line)


sys.exit(0)