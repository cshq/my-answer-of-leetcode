# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:31:47 2019

@author: THTF
"""

def intersect( nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    dic1,dic2={},{}
    for i in nums1:
        if i not in dic1:
            dic1[i]=1
        else:
            dic1[i]+=1
    for j in nums2:
        if j not in dic2:
            dic2[j]=1
        else:
            dic2[j]+=1
    res=[]
    for k in dic1:
        if k in dic2:
            res.extend(min(dic1[k],dic2[k])*[k])
    return res