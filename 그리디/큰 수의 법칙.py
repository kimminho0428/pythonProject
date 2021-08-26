# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:20:32 2021

@author: user
"""


n,m,k=map(int,input().split())
data = list(map(int,input().split()))
data.sort()
power=data[n-1]
weak=data[n-2]

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * power
result += (m-count) * weak

print(result)


            
        
        
