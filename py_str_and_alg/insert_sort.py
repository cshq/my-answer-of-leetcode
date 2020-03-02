# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:24:02 2019

@author: Administrator
"""

def insert_sort(alist):
    n=len(alist)
    for i in range(1,n):
        while alist[i]<alist[i-1] and i!=0:
            alist[i],alist[i-1]=alist[i-1],alist[i]
            i-=1
            
            
            
if __name__=="__main__":
    test_list=[9,7,22,11,18,5,95,31,76,7,23,12,33,45,23,12,2,100]
    print(test_list)
    insert_sort(test_list)
    print(test_list)
            
            