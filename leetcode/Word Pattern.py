# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:09:54 2019

@author: THTF
"""

def wordPattern(pattern,str):
    str_list=str.split(" ")
    str_dic={}
    j=0
    for i in str_list:
        if i not in str_dic:
            if pattern[j] in str_dic.values():
                return False
            #为了ac [“abbc”,"dog cat cat fish"]的case
            str_dic[i]=pattern[j]
            j+=1
        elif str_dic[i]!=pattern[j]:
            return False
        else:
            j+=1
    return True