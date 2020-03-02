# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 03:09:29 2019

@author: Administrator
"""
"""打家劫舍 House Robber
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的
房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。"""
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n=len(nums)
    if n==0:
        return 0
    if n==1:
        return nums[0]
    dp=[0]*n
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+nums[i])
    return dp[-1]

print(rob([2,1,1,2]))
"""状态转移方程为dp[i]=max(dp[i-1],dp[i-2]+nums[i])
注意有状态方程写程序的步骤思路
dp[i]表示到底i个元素(下标为0，对应list)时，所要的结果。
所以dp[0]=nums[0] ,dp[1]=max(nums[0],nums[1])



动态规划基本要素：①后面由前面决定，层层递推
②后面的不影响前面的
（very important)"""