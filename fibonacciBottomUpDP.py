# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 07:58:37 2022

@author: Riya Gupta
"""

'Print fibonacci series for Tn terms'

def fibonacciSeries(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(1, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp

n = int(input())
print(f"Fibonacci Series is: {fibonacciSeries(n)}")