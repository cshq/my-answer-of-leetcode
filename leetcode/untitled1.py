# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:22:09 2019

@author: THTF
"""

def wiggleMaxLength(nums):
    res=0
    flg=nums[1]-nums[0]
    for i in range(2,len(nums)):
        if flg>0:
            if nums[i]-nums[i-1]<0:
                res+=1
            else:
                continue
        if flg<0:
            if nums[i]-nums[i-1]>0:
                res+=1
            else:
                continue
        flg=nums[i]-nums[i-1]
    return res+2

print(wiggleMaxLength([1,7,4,9,2,5]))