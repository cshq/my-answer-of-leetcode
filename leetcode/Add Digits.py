# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:39:16 2019

@author: THTF
"""


def addDigits(num) :
    num=str(num)
    while len(num)>1:
        tmp=0
        for i in num:
            tmp=tmp+int(i)
        num=str(tmp)
    return int(num)
"""方法2"""
def addDigits2(num):
    while len(str(num))>1:
        num=eval("+".join(str(num)))
    return num