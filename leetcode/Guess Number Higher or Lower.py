# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:52:11 2019

@author: THTF
"""

def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n
    while left <= right:
        mid = left + (right - left) // 2
        # 猜测结果
        flag = guess(mid)
        if flag == -1:
            # 猜大了
            right = mid - 1
        elif flag == 1:
            # 猜小了
            left = mid + 1
        else:
            # 猜对了
            return mid