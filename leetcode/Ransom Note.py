# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:06:13 2019

@author: THTF
"""

def canConstruct( ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    from collections import Counter
    if not ransomNote:
        return True
    c1,c2=Counter(ransomNote),Counter(magazine)
    for i in c1:
        if  c1[i]>c2[i] or  i not in c2:
            return False
    return True
