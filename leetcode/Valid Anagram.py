# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:38:12 2019

@author: THTF
"""



def isAnagram(s,t):
    dic_s={}
    for i in s:
        if i not in dic_s:
            dic_s[i]=1
        else:
            dic_s[i]+=1
    for j in t:
        if j not in dic_s:
            return False
        else:
            dic_s[j]-=1
    for item in dic_s:
        if dic_s[item]!=0:
            return False
    return True