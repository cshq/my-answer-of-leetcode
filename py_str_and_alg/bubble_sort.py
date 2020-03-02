# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 13:03:56 2019

@author: Administrator
"""

#冒泡排序
def bubble_sort(list):
    n=len(list)
    for j in range(n-1):
        count=0
        for i in range(n-1-j):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                count+=1
        if count==0:
               break

if __name__=="__main__":
    test_list=[9,7,6,11,18,5,95,31,76,28,3,13,2,43,21,1,7]
    print(test_list)
    result=bubble_sort(test_list)
    print(test_list)
                