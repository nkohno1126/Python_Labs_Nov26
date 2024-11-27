#!  /use/bim/eng python3
# desctrittion: This script will demo howto ITERATE through files
# and the file system using an ITERATOR for Loop plus the glob moddule.

import sys
import glob
import os

if sys.platform == 'win32':
    home = os. environ['HOMEPATH']
    pattern = home + "\*"
else:
    home = os.environ['HOME']
    pattern = home + "/*"

print(pattern)

for files in glob.glob(pattern):
    if os.path.isfile(files):
        print(files, os.path.getsize(files))

