# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:28:37 2019

@author: THTF
"""


def isPowerOfTwo(n):
    if n==0:
        return False
    while n%2==0:
        n=n//2
    return n==1