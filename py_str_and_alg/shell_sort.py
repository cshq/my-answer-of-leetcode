# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:06:37 2019

@author: Administrator
"""

'''def shell_sort(a):
    n=len(a)
    gap=n//2
    while gap>0:
        j=0
        while j<gap:
            for i in range(gap+j,n,gap):
                while a[i]<a[i-gap] and i!=j:
                    a[i-gap],a[i]=a[i],a[i-gap]
                    i=i-gap
            j=j+1
        gap=gap//2
if __name__=="__main__":
    test_list=[9,7,22,11,18,5,95,31,76,7,23,12,33,45,23,12,2,100]
    print(test_list)
    shell_sort(test_list)
    print(test_list)'''
            
def shell_sort_better(a):
    n=len(a)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            while a[i]<a[i-gap] and i>=gap:
                a[i-gap],a[i]=a[i],a[i-gap]
                i=i-gap
            #j=j+1
        gap=gap//2
        #j=0
        #while j<gap:
        
if __name__=="__main__":
    test_list=[9,7,22,11,18,5,95,31,76,7,23,12,33,45,23,12,2,100,27,14,55]
    print(test_list)
    shell_sort_better(test_list)
    print(test_list)
           