# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:36:00 2019

@author: THTF
"""
import math
def isPowerOfThree(n):
    return n > 0 and 3 **round (math.log(n, 3)) == n
#math.log(243,3)计算机算出来为4.9999999，所以要加round防止这种情况
    
print(isPowerOfThree(243))