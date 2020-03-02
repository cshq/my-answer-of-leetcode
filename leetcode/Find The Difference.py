# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:13:07 2019

@author: THTF
"""

def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    p=sum(map(ord,s))
    q=sum(map(ord,t))
    q_p=q-p
    return chr(q_p)

#利用ACSII码相减再还原