# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:14:17 2019

@author: Administrator
"""

"""
搜索插入位置 Search Insert Position
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
示例 1:
输入: [1,3,5,6], 5
输出: 2
示例 2:
输入: [1,3,5,6], 2
输出: 1
示例 3:
输入: [1,3,5,6], 7
输出: 4
示例 4:
输入: [1,3,5,6], 0
输出: 0
"""
"""solution1 :normal method"""
def searchInsert(nums, target):
    if target>nums[-1]:
        return len(nums)
    if target<=nums[0]:
        return 0
    for i in range(len(nums)):
        if nums[i]<=target and nums[i+1]>=target:
            return i+1
print(searchInsert([1,3,5,7],8))

"""solution2: using Binary Search"""
def searchInsert2(nums, target):
        left = 0
        right = len(nums) - 1
        while left <=right:
            mid = left + (right - left) // 2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
print(searchInsert2([1,4,7,8,10],6))

"""solution3 using binary search"""
def searchInsert3(nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2 
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
"""注意比较solution2和solution3,一般用2"""



