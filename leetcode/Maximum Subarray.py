# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:14:05 2019

@author: Administrator
"""

"""最大子序和Maximum Subarray
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。"""
"""solution1:Dynamic Programming"""
def maxSubArray(nums):
    for i in range(1,len(nums)):
        subMaxSum=max(nums[i]+nums[i-1],nums[i])
        nums[i]=subMaxSum
    return max(nums)

print(maxSubArray([2,1,-3,4,-1,2,1,-5,4]))

"""solution2:逻辑推"""
def maxSubArray2(nums):
    sum=0
    Maxsum=nums[0]
    for i in range(len(nums)):
        sum+=nums[i]
        if sum>Maxsum:
            Maxsum=sum
        if sum<0:
            sum=0
    return Maxsum
print(maxSubArray2([2,1,-3,4,-1,2,1,-5,4]))

"""solution3:分治算法"""
#可以有 但是感觉该题适用性不强 因为可能横跨呀，分治算法思想可参考归并排序