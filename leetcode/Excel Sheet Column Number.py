# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:09:16 2019

@author: Administrator
"""
"""Excel表列序号Excel Sheet Column Number
给定一个Excel表格中的列名称，返回其相应的列序号。
例如，
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
示例 1:
输入: "A"
输出: 1
示例 2:
输入: "AB"
输出: 28
示例 3:
输入: "ZY"
输出: 701"""
def titleToNumber(s):
    res=0
    jinwei=-1
    for i in s[::-1]:
        jinwei+=1
        res=res+(ord(i)-64)*pow(26,jinwei)
    return res

if __name__=="__main__":
    print(titleToNumber("CCZCV"))