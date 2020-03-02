# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:31:16 2019

@author: Administrator
"""

def quick_sort(L,first,last):
    if first>=last:
        return
    mid_val=L[first]
    low=first
    high=last

    while low<high:
        while L[high]>=mid_val and low<high:
            high=high-1
        L[low]=L[high]
        while L[low]<mid_val and low<high :     
            low=low+1
        L[high]=L[low]
    L[low]=mid_val
    
    quick_sort(L,first,low-1)
    quick_sort(L,low+1,last)
    
    
if __name__=="__main__":
    test_list=[19,11,18,95,15,100,27,14,55]
    print(test_list)
    quick_sort(test_list,0,len(test_list)-1)
    print(test_list)
                
          
        