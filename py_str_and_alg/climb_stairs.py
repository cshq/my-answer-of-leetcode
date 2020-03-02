# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:06:57 2019

@author: Administrator
"""

def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n>2:
        return f(n-1)+f(n-2)
    
    
f(5)
print(f(5))
# 假定第一次跳的是一阶，那么剩下的是n-1个台阶，跳法是f(n-1)；假定第一次跳的是2阶，
#那么剩下的是n-2个台阶，跳法是f(n-2)；


#非递归，循环代替递归
def f(number):
    if number==1:
        return 1
    if number==2:
        return 2
    if number>2:
        a=1
        b=2
        while number-2>0:
            b,a=a+b,b
            number-=1
        return b
