# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 04:10:38 2022

@author: Riya Gupta
"""

"""
Binary Search Approach: works on sorted array
"""

def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid + 1
        if x <= arr[mid]:
            high = mid - 1
        else:
            low = mid
    return -1
    
arr = [10, 20, 30, 40, 60, 110, 120, 130, 170]

print(binarySearch(arr, 110))
print(binarySearch(arr, 175))