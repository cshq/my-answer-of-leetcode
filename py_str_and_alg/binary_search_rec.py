# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:51:16 2019

@author: Administrator
"""


    

def binary_search_rec(alist,item):
    n=len(alist)
    if n>0:
        mid=(n-1)//2
        if alist[mid]==item:
            return True
        elif item<alist[mid]:
            return binary_search_rec(alist[:mid],item)
           #return True
        elif item>alist[mid]:
            return binary_search_rec(alist[mid+1:],item)
          # return True
    return False

if __name__=="__main__":
    x=binary_search_rec([1,2,3,4,5,11,19,22,24],6)
    print(x)
