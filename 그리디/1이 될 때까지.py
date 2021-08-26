# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 12:00:22 2021

@author: user
"""

import time
n,k=map(int,input().split())
count = 0

start = time.time()

while(True):
    if(n>=k):
        if(n % k == 0):
            n /= k
            count += 1
        elif(n % k != 0):
            count += n%k
            n -= n%k
    elif(n>1):
        n -= 1
        count += 1
    else:
        break
print(count)

end = time.time()
print(end-start)
