# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:03:19 2019

@author: Administrator
"""

"""
Reverse Integer
整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""
"""solution 1 :纯数学"""
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    j=0
    if x<0:
        x=-x
        while x:
            j=j*10+x%10
            x=x//10
        j=-j
    else:
        while x:
            j=j*10+x%10
            x=x//10
    if abs(j)>2**31-1:
        return 0
    else:
        return j
print(reverse(-123446767623123575))
"""solution2 :字符串"""
def reverse2(x):
    if x==0:
        return 0
    str_x=str(x)
    rev_x=str_x.strip("0")[::-1]
    if rev_x[-1]=="-":
        rev_x=rev_x.strip('-')
        list_rev_x=list(rev_x)
        list_rev_x.insert(0,"-")
        rev_x=''.join(list_rev_x)
        rev_x=int(rev_x)
    rev_x=int(rev_x)
    if abs(rev_x)>2**31:
        return 0
    else:
        return rev_x
print(reverse2(123))

"""solution3:字符串(用[::]，用int处理负号)"""    
def reverse3(x):
    if x==0:
        return 0
    if x<0:
        str_x=str(-x)
        rev_x=str_x[::-1].strip("0")
        rev_x=-int(rev_x)
    else:
        str_x=str(x)
        rev_x=str_x[::-1].strip("0")
        rev_x=int(rev_x)
    if abs(rev_x)>2**31:
        return 0
    else:
        return rev_x



         