# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:16:44 2019

@author: THTF
"""

def intersection(nums1,nums2):
    set_nums1=set(nums1)
    set_nums2=set(nums2)
    res=[]
    for i in set_nums1:
        if i in set_nums2:
            res.append(i)
    return res