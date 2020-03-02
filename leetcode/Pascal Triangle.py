# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:13:54 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:24:50 2019

@author: Administrator
"""

"""杨辉三角  Pascal's Triangle
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
def generate(num_rows):
    triangle = []

    for row_num in range(num_rows):
        # The first and last row elements are always 1.
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle

if __name__=="__main__":
    print(generate(1))
"""自己写的"""
def generate(num_rows):
    triangle=[]
    if num_rows==1:
        triangle=[[1]]
    if num_rows==2:
        triangle=[[1],[1,1]]
    if num_rows>=3:
        triangle=[[1],[1,1]]
        for i in range(3,num_rows+1):
            li=[None for _ in range(i)]
            li[0],li[-1]=1,1
            for j in range(1,i-1):
                li[j]=triangle[i-2][j-1]+triangle[i-2][j]
            triangle.append(li)
    return triangle

print(generate(4))
