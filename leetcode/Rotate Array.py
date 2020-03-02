# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:31:52 2019

@author: Administrator
"""
"""旋转数组Rotate Array
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。"""
"""solution1:"""
def rotate(nums, k):
    k%=(len(nums))
    for _ in range(k):
        nums.insert(0,nums.pop())

nums=[1,2,3,4,5,6,7]
rotate(nums,3)
print(nums)
"""solution2:"""
def rotate2(nums, k):
#    nums=nums[-k:]+nums[:len(nums)-k]这个过不了[2]这种的
    k%=(len(nums))
    nums[:]= nums[-k:] + nums[0:-k]
    

    