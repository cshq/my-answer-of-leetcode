# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:45:48 2019

@author: Administrator
"""
"""爬楼梯 Climbing Stairs
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶"""
"""solution1 :recursion:递归方法 时空复杂度有点高"""
def climbStairs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return climbStairs(n-1)+climbStairs(n-2)
    
print(climbStairs(6))

"""solution2:Dynamic programming"""
#dp[i]=dp[i-1]+dp[i-2] 状态转移公式
def climbStairs2(n):
    if n==1:
        return 1
    if n==2:
        return 2
    dp=[]
    dp.append(1)
    dp.append(2)
    for i in range(2,n):
        dp.append(dp[i-1]+dp[i-2])
    return dp[i]

print(climbStairs2(5))

"""solution 3"""
def climbStairs3(n):
    if n==1:
        return 1
    if n==2:
        return 2
    p=1
    q=2
    c=0
    for i in range(2,n):
        c=q
        q=p+q
        p=c
        
    return q
print(climbStairs3(5))
#不定义c 而采用 p,q=q,p+q也行
    