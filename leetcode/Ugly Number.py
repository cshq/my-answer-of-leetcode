# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:40:57 2019

@author: THTF
"""

def isUgly(num):
    if num==0:
        return False
    while num%2==0:
        num/=2
    while num%3==0:
        num/=3
    while num%5==0:
        num/=5
    return num==1