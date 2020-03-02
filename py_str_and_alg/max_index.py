# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:53:20 2019

@author: Administrator
"""

def f(alist):
    max_index=0
    n=len(alist)
    for i in range(0,n-1):
        if alist[max_index]<alist[i]:
            max_index=i
    return max_index

if __name__=="__main__":
    max_index_test=f([1,2,3,7,2,6,1,0,11,4])
    print(max_index_test)