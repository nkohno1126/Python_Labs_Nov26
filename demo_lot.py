#! /use/bin/eng python3
# Autor: NKohno
# Version:1.0
# numbers

import random

lotto = []

while len(lotto)< 6:
    num = random.randint(1,50)
    if num not in lotto:
        lotto.append(num)
    else:
        print('duplicate =', lotto, num)



print(lotto)