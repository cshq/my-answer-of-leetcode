# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:34:47 2019

@author: THTF
"""


def minSubArrayLen(s,nums):
    if sum(nums) == s:
        return len(nums)
    if sum(nums) < s:
        return 0
    left=0
    tmp_sum=0
    res=len(nums)
    for right in range(len(nums)):
        tmp_sum+=nums[right]
        while tmp_sum>=s:
            tmp_sum-=nums[left]
            res=min(res,right-left+1)
            left+=1
    return res