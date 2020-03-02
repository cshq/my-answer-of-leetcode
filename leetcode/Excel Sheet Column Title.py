# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:36:20 2019

@author: Administrator
"""

"""Excel表列名称Excel Sheet Column Title
给定一个正整数，返回它在 Excel 表中相对应的列名称。
例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:
输入: 1
输出: "A"
示例 2:
输入: 28
输出: "AB"
示例 3:
输入: 701
输出: "ZY"""

"""solution1 :自己写的"""
def convertToTitle(n):
    ex_dic={0:"",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7: 'G', 8: 'H',
                    9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P',
                    17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
                    25: 'Y', 26: 'Z'}
    res=''
    while n//26:
        if n%26==0:
            res="Z"+res
            n=n//26-1
        else:
            res=ex_dic.get(n%26)+res
            n=n//26
    return ex_dic.get(n)+res
print(convertToTitle(29*26))

"""solution2: ASCII Code"""
def convertToTitle(n):
    res = ""
    while n:
        n,y=divmod(n,26)
        if y==0:
            n=n-1
            y==26
        res=chr(y+64)+res
    return res
"""solution3:类似上面"""
def convertToTitle(self, n: int) -> str:
    res = ""
    while n:
        n -= 1
        n, y = divmod(n, 26) 
        res = chr(y + 65) + res
    return res


"""https://leetcode-cn.com/problems/excel-sheet-column-title/solution/shi-jin-zhi-zhuan-26jin-zhi-by-powcai/"""

