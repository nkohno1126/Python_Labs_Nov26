#! /use/bin/env python3


import sys
# New code
import shelve


shelve.open(r"C:\Users\Kohno\project\Python_Labs_Nov26\demo")

movies = { 'chris': ['die hard', 'trainspotting', 'barbie'],
           'tom': ['12 strong', 'forest gump', 'the matrix'],
           'andrius': ['gladiator', 'the boondock saints', 'con air'],
           'winson': ['top gun', 'terminator', 'pretty woman']}

tv_series = { 'chris': ['walking dead', 'yellowstone'],
           'tom': ['breaking bad', 'the boys'],
           'andrius': ['outlander', 'dads army'],
           }

books = { 
           'andrius': ['dummys guide to python'],
           'winson': ['extreme ironing']}

with shelve.open(r"C:\Users\Kohno\project\Python_Labs_Nov26\media") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"C:\Users\Kohno\project\Python_Labs_Nov26\media") as db:
    print(f'chris favourite movies are {db['movies']['chris']}')
    print(f'tom favourite movies are {db['tv_series']['tom'][0]}')
    print(f'winson favourite movies are {db['tv_series']['tom'][0]}')