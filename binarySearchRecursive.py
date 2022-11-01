# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 07:49:20 2022

@author: Riya Gupta
"""

def binarySearch(arr, x, p, r):
    low = p
    high = max(p, r)
    if low < high:
        mid = (low + high)//2
        if x == arr[mid]:
            return mid + 1
        if x < arr[mid]:
            return binarySearch(arr, x, low, mid)
        else:
            return binarySearch(arr, x, mid+1, high)
    return -1

arr = [10, 20, 30, 40, 60, 110, 120, 130, 170]

print(binarySearch(arr, 110, 0, len(arr)))
print(binarySearch(arr, 175, 0, len(arr)))