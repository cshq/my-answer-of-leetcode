# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 17:00:01 2019

@author: Administrator
"""
#选择排序
def select_sort(list):
    n=len(list)
    for j in range(n-1):
 #       min=list[j]
        for i in range(j+1,n):
            if list[i]<list[j]:
                list[i],list[j]=list[j],list[i]

if __name__=="__main__":
    test_list=[9,7,22,11,18,5,95,31,76,7,23,12,33,45,23,12,2]
    print(test_list)
    select_sort(test_list)
    print(test_list)
                