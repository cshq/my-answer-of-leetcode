# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:33:24 2019

@author: Administrator
"""
"""阶乘后的零Factorial Trailing Zeroes
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零."""



"""0是由2*5形成的，所以因式中的5的数量就是结果，注意25有两个5,125有三个5......"""
"""solution1:my way"""
def trailingZeroes(n):
    res=0
    for i in range(0,n+1,5):
        if i==0:
            continue
        while i%5==0:
            i=i//5
            res+=1
    return res
"""solution2:better way"""
def trailingZeroes2(n):
    res=0
    while n//5:
        """while n>=5也许更好,两者等价，计算量更小"""
        res+=n//5
        n//=5
    return res

print(trailingZeroes2(125))