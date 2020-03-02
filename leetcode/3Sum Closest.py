# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 13:50:02 2019

@author: THTF
"""

def threeSumClosest(nums,target):
    nums.sort()
    n=len(nums)
    res=float("inf")
    for i in range(n):
        left=i+1
        right=n-1
        while left<right:
            cur_sum=nums[i]+nums[left]+nums[right]
            if cur_sum==target:
                return target
            elif cur_sum<target:
                if abs(cur_sum-target)<abs(res-target):
                    res=cur_sum
                left+=1
            else:
                if abs(cur_sum-target)<abs(res-target):
                    res=cur_sum
                right-=1
    return res

#类似3sum

