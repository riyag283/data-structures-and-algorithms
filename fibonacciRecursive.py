# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 08:03:11 2022

@author: Riya Gupta
"""

'Fibonacci'

def fibonacci(n):
    if n <= 1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(f"Fibonacci Tn value: {fibonacci(n)}")