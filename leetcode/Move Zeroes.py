# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:39:57 2019

@author: THTF
"""

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] , nums[i]= nums[i] , nums[j]
            j += 1
            
    

k=[0,1,3,4,0,8,0]
moveZeroes(k)
print(k)