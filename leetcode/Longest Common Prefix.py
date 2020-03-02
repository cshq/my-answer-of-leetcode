# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:05:41 2019

@author: Administrator
"""

"""最长公共前缀Longest Common Prefix
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。"""
"""solution """
def longestCommonPrefix(strs):
    nums_list=[]
    n=len(strs)
    for i in strs:
        nums_list.append(len(i))
    min_num=min(nums_list)
    i=0
    for i in range(min_num):
        for j in range(n-1):
            if strs[j][i]!=strs[j+1][i]:
                return strs[0][:i]
    return strs[0][:min_num]
#应该为min_num 而非 i+1 因为 ["abab","aba",""]结果不对
print(longestCommonPrefix(["flowerss","flower","flower"]))


"""uing while"""
def longestCommonPrefix1(strs):
    nums_list=[]
    n=len(strs)
    for i in strs:
        nums_list.append(len(i))
    min_num=min(nums_list)
    i=0
    while i<min_num:
        for j in range(n-1):
            if strs[j][i]!=strs[j+1][i]:
                return i
        i+=1
    return min_num

