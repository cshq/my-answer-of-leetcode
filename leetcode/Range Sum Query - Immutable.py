# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:42:00 2019

@author: THTF
"""
class NumArray:

    def __init__(self,nums): 
        self.nums = nums
        sum_=0
        n = len(self.nums)
        target =[]
        for i in range(n):
            sum_ += nums[i]
            target.append(sum_)
        self.__target=target
#        如果没有这一句，下面的target也不加self.   那么的话就会报错
    def sumRange(self,i,j):            
        return self.__target[j]-self.__target[i]+self.nums[i]
    
    
ns=NumArray([-3,2,4,6,14,8])
print(ns.sumRange(2,4))