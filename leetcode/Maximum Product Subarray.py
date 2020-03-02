# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:17:50 2019

@author: THTF
"""

def maxProduct(nums):
    if not nums:
        return
    res=nums[0]
    pre_max=nums[0]
    pre_min=nums[0]
    for num in range(1,len(nums)):
        cur_max=max(pre_max*nums[num],pre_min*nums[num],nums[num])
        cur_min=min(pre_max*nums[num],pre_min*nums[num],nums[num])
        res=max(res,cur_max)
        pre_max=cur_max
        pre_min=cur_min
    return res


"""https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/"""

def maxProduct2(nums):
    reverse_nums = nums[::-1]
    for i in range(1, len(nums)):
        if nums[i-1]:
            nums[i]*=nums[i-1]
        if reverse_nums[i-1]:
            reverse_nums[i]*=reverse_nums[i-1]
    return max(nums + reverse_nums)

"""正反各来一次,遇到0就重置，不需要1 ，因为本身就是乘以1"""