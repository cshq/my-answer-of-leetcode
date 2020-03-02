# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:17:35 2019

@author: THTF
"""

"""荷兰国旗问题"""
"""solution1 经典三路快排"""
def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    p0,cur,p2=0,0,len(nums)-1
    while p0<p2:
        if nums[cur]==1:
            cur+=1
        elif nums[cur]==0:
            nums[cur],nums[p0]=nums[p0],nums[cur]
            cur+=1
            p0+=1
        elif nums[cur]==2:
            nums[cur],nums[p2]=nums[p2],nums[cur]
            p2-=1
    
"""solution2 重写数组"""
def sortColors2(nums):
    m,n,q=0
    for i in nums:
        if i==0:
            m+=1
        elif i==1:
            n+=1
        elif i==2:
            q+=1
    k=0
    while k<m:
        nums[k]=0
        k+=1
    while k<m+n:
        nums[k]=1
        k+=1
    while k<m+n+q:
        nums[k]=2
        k+=1
    