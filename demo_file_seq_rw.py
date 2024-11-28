#! /use/bin/env python3

# demo howto open, and read, write, and append and close a text file
import sys
# New code

movies = { 'chris': ['die hard', 'trainspotting', 'barbie'],
           'tom': ['12 strong', 'forest gump', 'the matrix'],
           'andrius': ['gladiator', 'the boondock saints', 'con air'],
           'winson': ['top gun', 'terminator', 'pretty woman']
}



fin_out= open (r"C:\Users\Kohno\project\Python_Labs_Nov26\movies.txt", mode = 'rt')

#text = fin_out.readlines()

for line in fin_out:
    print(line, end = '')


#print(text)

fin_out.close()


sys.exit(0)