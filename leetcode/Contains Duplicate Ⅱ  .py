# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:27:02 2019

@author: Administrator
"""

"""存在重复元素 II Contains Duplicate II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false"""
def containsNearbyDuplicate(nums, k):
    num_dic={}
    j=0
    for i in nums:
        if i not in num_dic:
            num_dic[i]=j
            j+=1
        elif j-num_dic[i]<=k:
            return True
            """一旦找到 直接返回True"""
        else:
            num_dic[i]=j
            j+=1
    return False
    """遍历以后没找到 返回False"""
print(containsNearbyDuplicate([1,2,3,1,2,3],2))
