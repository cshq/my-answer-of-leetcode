# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:26:33 2019

@author: Administrator
"""
"""两数相除 Divide Two Integers
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。"""

def divide(dividend, divisor):
    res=0
    abs_dividend=abs(dividend)
    abs_divisor=abs(divisor)
    while abs_dividend>=abs_divisor:
        mult=abs_divisor
        md=1
        while abs_dividend>=mult:
            abs_dividend-=mult
            res=res+md
            md=md<<1
            mult=mult<<1
#    主要的完成了 后面的是细枝末节
    if dividend<0 and divisor<0:
        if res==2<<30:
            return res-1
        else:
            return res
    elif dividend>0 and divisor>0:
        if res==2<<30:
            return res-1
        else:
            return res
    else:
        return -res

    
print(divide(-11111,-1))