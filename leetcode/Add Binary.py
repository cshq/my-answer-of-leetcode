# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:51:07 2019

@author: Administrator
"""

"""二进制求和Add Binary
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。
示例 1:
输入: a = "11", b = "1"
输出: "100"
示例 2:
输入: a = "1010", b = "1011"
输出: "10101"""
"""solution1：built_in function"""
def addBinary(a, b):
    a,b=int(a,2),int(b,2)
    res=bin(a+b)[2:]
    return res
    
print(addBinary("1010","1011"))

"""solution2: original realize"""

def addBinary(a,b):

    # 短字符串前端补零，保证两者长度相等
    if len(a) > len(b):
        b = '0'* (len(a)-len(b)) + b
    elif len(a) < len(b):
        a = '0'* (len(b) - len(a)) + a

    zes, carry = '', '0'
    for a_, b_ in reversed(list(zip(a, b))):

        if a_ == '0' and b_ == '0':                                 # 当前位两个数都是0
            mm = carry
            carry = '0'
        elif a_ == '1' and b_ == '0' or a_ == '0' and b_ == '1':    # 当前位两个数不同
            mm = '1' if carry == '0' else '0'
#            carry = '1' if carry == '1' else '0'
        else:                                                       # 当前位两个数都是1
            mm = '1' if carry == '1' else '0'
            carry = '1'

        zes=(mm+zes
             )

    if carry == '1':                                                # 如果还有进位
        zes = '1' + zes
        
    return zes
print(addBinary("11","1"))

    