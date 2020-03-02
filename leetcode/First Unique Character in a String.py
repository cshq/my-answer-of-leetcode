# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:00:43 2019

@author: THTF
"""

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    dics={}
    for i in s:
        dics[i]=dics[i]+1 if i in dics else 1
    for i,c in enumerate(s):
        if c in dics and dics[c]>0:
            return i
#        enumerate函数在这里挺好用
    return -1

"""也可用有序词典"""