#! /use/bin/env python3

# safer way of managing file handles using a context resource maneger (with statement)
import sys
# New code
import re
#open file handle for reading in text mode
with open(r"C:\Users\Kohno\project\Python_Labs_Nov26\movies.txt", mode = 'rt') as fin_out:
    for line in fin_out:
        print(line, end='')
port_used = set()
all_ports=set(range(1,201))
with open(r"C:\Users\Kohno\Desktop\services", mode = 'rt') as fin_out:
    for line in fin_out:
        m=re.search(r'(\d+)/(tcp|udp)',line)
        if m:
            port = int(m.group(1)) 
            if port <=200:
                
                port_used.add(m)
print(port_used)
        
      

