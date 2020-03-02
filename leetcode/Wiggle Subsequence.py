# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:32:44 2019

@author: THTF
"""

def wiggleMaxLength(nums):
    if not nums:
        return 0
    if len(nums)==1:
        return 1
    s=0
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]!=0:
            s=i
            break
        else:
            continue
    if s==0:
        return 1
    """主要为了隔开前面连续的相同的数字如[0,0,0,0]以及[3,3,3,3,4,6,2,10]等情况,这样[3,3,3,3,4,6,2,10]就会变成[4,6,2,10]"""
    res=0
    flg=nums[s]-nums[s-1]
    for i in range(s,len(nums)):
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