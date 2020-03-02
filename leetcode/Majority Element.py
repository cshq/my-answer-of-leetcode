# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:31:45 2019

@author: Administrator
"""
"""求众数Majority Element
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2"""
"""solution1：字典遍历"""
def majorityElement(nums):
    nums_dic={}
    n=len(nums)
    for i in nums:
        if i not in nums_dic:
            nums_dic[i]=1
        else:
            nums_dic[i]+=1
    return [k for k,v in nums_dic.items() if v>n//2][0]
#items()返回的是一个可迭代的元祖对象，像表示出来 还是要list下
"""solution2:Boyer-Moore voting"""
def majorityElement2(nums):
    count=0
    maj_el=nums[0]
    n=len(nums)
    for i in range(n):
        if nums[i]==maj_el:
            count+=1
        else:
            count-=1
        if count==0:
            maj_el=nums[i+1]
    return maj_el
"""solutuon2_2"""
def majorityElement2_2(nums):
    count=0
    maj_el=None
    for i in nums:
        if count==0:
            maj_el=i
        count+=(1 if i==maj_el else -1)
    return maj_el
        
print(majorityElement2([2,2,1,1,1,2,2]))
            
            