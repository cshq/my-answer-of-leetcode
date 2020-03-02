# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:42:31 2019

@author: THTF
"""


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    left=1
    right=n
    while left<right:
        mid=left+(right-left)//2
        if isBadVersion(mid)==False:
            left=mid+1
        else:
            right=mid
    return left