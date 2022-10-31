# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 04:01:46 2022

@author: Riya Gupta
"""

"""
The following search approach will take O(n) time.
"""

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [2,3,19,1,5,6,7,4]
print(linearSearch(arr, 19))
print(linearSearch(arr, 18))