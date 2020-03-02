# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:37:42 2019

@author: THTF
"""

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n=len(matrix[0])
    m=len(matrix)
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                # matrix[i]=0
                for k in range(m):
                    if matrix[k][j]!=0:
#                        如果这里没有这个if 那么后面的0就会被淹没掉
                        matrix[k][j]=''
                for k in range(n):
                    if matrix[i][k]!=0:
                        matrix[i][k]=''
    for i in range(m):
        for j in range(n):
            if matrix[i][j]=='':
                matrix[i][j]=0 