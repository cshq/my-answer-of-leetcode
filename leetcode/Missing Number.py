# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:41:48 2019

@author: THTF
"""

def missingNumber(nums):
    return (len(nums)+1)*(len(nums))//2-sum(nums)