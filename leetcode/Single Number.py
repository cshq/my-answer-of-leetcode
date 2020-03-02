# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:43:17 2019

@author: Administrator
"""
"""只出现一次的数字Single Number
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
示例 2:
输入: [4,1,2,1,2]
输出: 4"""
"""solution1 :集合"""
def singleNumber(nums):
    s=set()
    for i in nums:
        if i not in s:
            s.add(i)
        else:
            s.remove(i)
    return s.pop()

print(singleNumber([4,1,2,1,2]))

"""solution 2 :列表"""
def singleNumber2(nums):
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()
#时间复杂度O(n^2)  遍历*判断in
"""solution 3：字典"""
def singleNumber3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1
    return hash_table.popitem()[0]
"""solutuin 4：字典"""
def singleNumber4(nums):
    hash_table={}
    for i in nums:
        if i not in hash_table:
            hash_table[i]=1
        else:
            hash_table.pop(i)
    return hash_table.popitem[0]
#时间复杂度：O（n^2)
"""solution 5: 位运算"""
def singleNumber5(nums):
        a = 0
        for i in nums:
            a ^= i
        return a