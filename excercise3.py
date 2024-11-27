import sys

pin='2222'
n = 3
i=0
while i<n:
    
    supplied_pin = input('Enter your pin: ')
    if supplied_pin == pin:
        print('Succeed')
        
        break
    else: 
        print('fail')
        i += 1
    

    
    