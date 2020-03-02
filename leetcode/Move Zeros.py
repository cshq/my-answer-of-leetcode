# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:44:10 2019

@author: THTF
"""


def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in nums:    
        if i==0:
            nums.remove(i)
            nums.append(i)
    return nums



def moveZeroes2(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] , nums[i]= nums[i] , nums[j]
            j += 1