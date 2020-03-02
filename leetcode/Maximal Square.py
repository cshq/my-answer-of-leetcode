# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:32:08 2019

@author: THTF
"""

def maximalSquare(matrix):
    length=0
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    dp=[[0]*len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='1':
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                length=max(length,dp[i][j])
    return length*length


"""dp，注意理解题目的意思吧,可以尝试暴力破解（官方题解) 其实也可行，并锻炼编程能力"""
"""https://leetcode-cn.com/problems/maximal-square/solution/zhi-xing-yong-shi-100-ms-zai-suo-you-python3-ti-ji/"""