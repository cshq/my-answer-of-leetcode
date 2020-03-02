# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:29:20 2019

@author: THTF
"""

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n=len(matrix[0])
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
#            原地转置矩阵
    for i in range(n):
        matrix[i].reverse()
#        反转每一行
        
matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
rotate(matrix)
print(matrix)