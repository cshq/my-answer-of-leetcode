# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:58:40 2019

@author: THTF
"""

"""solution1 : 双指针"""
def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    point_s=0
    point_t=0
    ls,lt=len(s),len(t)
    while point_s<ls and point_t<lt:
        if s[point_s]==t[point_t]:
            point_s+=1
        point_t+=1
    return point_s==ls
#这里用for循环不大好写，可以尝试下
