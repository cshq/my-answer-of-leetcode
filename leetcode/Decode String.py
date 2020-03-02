# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:37:06 2019

@author: THTF
"""


def decodeString(self, s: str) -> str:   
    res=''
    stack=[]
    multi=0
    for i in s:
        if i in '0123456789':
            multi = multi * 10 + int(i)    
        elif i=='[':
            stack.append([multi,res])
            res,multi='',0
        elif i==']':
            cur_multi,last_str=stack.pop()
            res=last_str+cur_multi*res
        else:
            res+=i
    return res

"""https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/"""
"""有点难以想到"""