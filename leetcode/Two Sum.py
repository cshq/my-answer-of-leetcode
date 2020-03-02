# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:29:31 2019

@author: Administrator
"""

"""Two Sum 两数之和
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""
"""first solution O(n^2)"""

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return( [i,j])
            
a=two_sum([2,7,8,22,11],29)
print(a)


"""second solution  using dic O(n)"""
def two_sum_2(nums,target):
    n_dict={}
    for i,element in enumerate(nums):
        if element not in n_dict:
            n_dict[target-element]=i
        else:
            return [n_dict[element],i]
        
a=two_sum_2([2,7,8,22,11],29)
print(a)     
