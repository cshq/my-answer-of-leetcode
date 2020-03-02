# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:50:37 2019

@author: THTF
"""

def threeSum(nums):
    res=[]
    nums.sort()
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        # if nums[i]>0:
        #     break
        n=i+1
        m=len(nums)-1
        while n<m:
            if nums[i]+nums[n]+nums[m]==0:
                res.append([nums[i],nums[n],nums[m]])
                while n<m and nums[n]==nums[n+1]:
                    n+=1
                while n<m and nums[m]==nums[m-1]:
                    m-=1
                n+=1
                m-=1
            elif nums[i]+nums[n]+nums[m]<0:
                n+=1
            else:
                m-=1
    return res

#排序复杂度nlogn,双指针n^2.所以最后是n^2
#绝大多数限定条件都是为了防止越界
