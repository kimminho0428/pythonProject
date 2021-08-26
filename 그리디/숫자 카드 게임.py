# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:15:12 2021

@author: user
"""

n, m = map(int, input().split())
arr = []
power = 0

for i in range(n):
    arr.append(list(map(int, input().split())))

    min_value = min(arr[i])
    power = max(min_value, power)
print(power)
