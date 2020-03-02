# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:51:51 2019

@author: THTF
"""

def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    left=0
    right=num
    mid=num//2
    while left<=right:
        if mid**2<num:
            left=mid+1
        elif mid**2>num:
            right=mid-1
#            此处应用if，输入14就会返回True，因为if if else这种他会将第一个if单独处理，else也只是else第二个if,
#            但是如果是if elif else这种就是全部互斥，一个通过了就不会执行后面了,当然if elif else 后面再接if，这个if还是会执行
        else:
            return True
        mid=left+(right-left)//2
    return False

