# safer way of managing file handles using a context resource maneger (with statement)
import sys
# New code


SOF = 0
CUR = 1
EOF = 2


#open file handle for reading in text mode
with open(r"C:\Users\Kohno\project\Python_Labs_Nov26\movies.txt", mode = 'rt') as fin_out:
    for line in fin_out:
        print(line, end='')


# with open(r"C:\Users\Kohno\project\Python_Labs_Nov26\movies.txt", mode = 'rt') as fin_out:
    fin_out.seek(90, SOF)
    text = fin_out.read(30)
    print(f'text at position {fin_out.tell() - len(text)} = {text}')

    fin_out.seek(135, SOF)
    text = fin_out.read(30)
    print(f'text at position {fin_out.tell() - len(text)} = {text}')

    print('-'*60)

with open(r"C:\Users\Kohno\project\Python_Labs_Nov26\movies.txt", mode = 'rb') as fh_data:
    fh_data.seek(-90, EOF)
    text = fh_data.read(30)
    print(f'text at position {fh_data.tell() - len(text)} = {text}')

    fh_data.seek(-60, CUR)
    text = fh_data.read(30)
    print(f'text at position {fh_data.tell() - len(text)} = {text}')