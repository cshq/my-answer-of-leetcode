# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:36:37 2019

@author: Administrator
"""

def binary_search(alist,item):
    n=len(alist)
    first=0
    last=n-1
    while first<=last:
        mid=(first+last)//2
        if item<alist[mid]:
            last=mid-1
        elif item>alist[mid]:
            first=mid+1
        else:
            return True
    return False



    
   

            
    