# safer way of managing file handles using a context resource maneger (with statement)
import sys
import pprint
import pickle
import gzip # 

# New code how to peserve one python object to a pickle file 
movies = { 'chris': ['die hard', 'trainspotting', 'barbie'],
           'tom': ['12 strong', 'forest gump', 'the matrix'],
           'andrius': ['gladiator', 'the boondock saints', 'con air'],
           'winson': ['top gun', 'terminator', 'pretty woman']}

SOF = 0
CUR = 1
EOF = 2


#open file handle for reading in text mode
#with open(r"C:\Users\Kohno\project\Python_Labs_Nov26\movies.p", mode = 'wb') as fin_out:

with gzip.open(r"C:\Users\Kohno\project\Python_Labs_Nov26\movies.pgz", mode = 'wb') as fin_out:
    pickle.dump(movies,fin_out, protocol = 3)
    pickle.dump(movies,fin_out, pickle.DEFAULT_PROTOCOL)
    #pickle.dump(movies,fin_out, protocol = 3)


#with open(r"C:\Users\Kohno\project\Python_Labs_Nov26\movies.pgz", mode = 'rb') as fh_data:
with gzip.open(r"C:\Users\Kohno\project\Python_Labs_Nov26\movies.pgz", mode = 'rb') as fh_data:
    films = pickle.load(fh_data)

pprint.pprint(movies)
print('-'*60)
pprint.pprint(movies)