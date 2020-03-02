# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:39:45 2019

@author: THTF
"""

def rob(nums):
    if not nums : 
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums)==2:
        return max(nums[0],nums[1])
    def helper(li):
        if not li :
            return 0
        if len(li)==1:
            return li[0]
        if len(li)==2:
            return max(li[0],li[1])
        n = len(li)
        dp = [0] * n
        dp[0] = li[0]
        dp[1]=max(li[0],li[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + li[i])
        return dp[-1]
    return max(helper(nums[1:]), helper(nums[:-1]))

"""动态规划，相对于不带首尾相连的只需要分类讨论即可。注意定义的新函数，为了防止直接return 出来"""