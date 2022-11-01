# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 08:11:09 2022

@author: Riya Gupta
"""

def fibonacci(n, dp):
    if n <= 1:
        dp[n] = n
    if dp[n] is None:
        dp[n] = fibonacci(n-1, dp) + fibonacci(n-2, dp)
    return dp[n]

n = int(input())
dp = [None] * (n+1)
print(f"Fibonacci Tn is: {fibonacci(n, dp)}")