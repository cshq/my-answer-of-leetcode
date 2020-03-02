# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:33:45 2019

@author: Administrator
"""
"""同构字符串 Isomorphic Strings
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true"""
"""solution1"""
def isIsomorphic1(s,t):
    str_dic={}
    j=0
    for i in s:
        if i not in str_dic:
            str_dic[i]=t[j]
            j+=1
        elif str_dic[i]==t[j]:
            j+=1
        elif str_dic[i]!=t[j]:
            return False
    str_dic2={}
    j=0
    for i in t:
        if i not in str_dic2:
            str_dic2[i]=s[j]
            j+=1
        elif str_dic2[i]==s[j]:
            j+=1
        elif str_dic2[i]!=s[j]:
            return False
    return True
"""solution2"""
def isIsomorphic2(s,t):
    str_dic={}
    j=0
    for i in s:
        if i not in str_dic:
            str_dic[i]=t[j]
            j+=1
        elif str_dic[i]==t[j]:
            j+=1
        elif str_dic[i]!=t[j]:
            return False
        
    return len(str_dic.values())==len(set(str_dic.values()))
    
    
"""solution3"""
def isIsomorphic3(s,t):
    dic = {}
    for i in range(len(t)):
        if s[i] not in dic: 
            dic[s[i]] = t[i]
        elif s[i] in dic:
            if dic[s[i]] != t[i]:
                return False          # 如果出现s中相同的字母映射到t中两个不同的字母，返回False
    return len(dic.values()) == len(set(dic.values()))  