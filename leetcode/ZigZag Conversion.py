# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:09:49 2019

@author: THTF
"""


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows < 2:
         return s
    res = ["" for _ in range(numRows)]
    i=0
    go_down=False
    for x in s:
        res[i]=res[i]+x
        if i==0 or i==numRows-1:
            go_down=not go_down
        if go_down:
            i+=1
        else:
            i-=1
    res=''.join(res)
    return res



s="leetcode"
print(convert(s))

"""go_down 控制方向 很精髓"""