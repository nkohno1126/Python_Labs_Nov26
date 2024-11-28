#! /use/bin/env python3

# safer way of managing file handles using a context resource maneger (with statement)
import sys
# New code

#open file handle for reading in text mode
with open(r"C:\Users\Kohno\project\Python_Labs_Nov26\movies.txt", mode = 'rt') as fin_out:
    for line in fin_out:
        print(line, end='')

