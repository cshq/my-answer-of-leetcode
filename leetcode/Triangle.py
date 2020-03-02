# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:00:02 2019

@author: THTF
"""

def minimumTotal(triangle):
    if not triangle:
        return 0
    if len(triangle)==1:
        return triangle[0][0]
    n=len(triangle)
    for i in range(1,n):
        for j in range(0,i+1):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
    return min(triangle[-1])


"""对于每个数字用dp,而非每行，每行比较难处理"""