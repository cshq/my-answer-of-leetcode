# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:45:47 2019

@author: Administrator
"""

""" 最后一个单词的长度Length of Last Word
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串。
示例:
输入: "Hello World"
输出: 5"""
"""solution1"""
def lengthOfLastWord(s):
    s=s.strip()
    if s=="":
        return 0
    los=len(s)
    a=s[::-1]
    k=0
    while a[k]!=" ":
        k+=1
        if k>=los:
            return los
    return k
print(lengthOfLastWord("aaaaa bb   "))
"""solution2:using split"""
def lengthOfLastWord2(s):
    return len(s.rstrip().split(" ")[-1])

print(lengthOfLastWord("aaaaa bb   "))
