# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:35:44 2019

@author: Administrator
"""

"""MergeSort:归并排序"""
def mergeSort(li):
    if len(li)==1:
        return li
    mid=len(li)//2
    left=li[:mid]
    right=li[mid:]
    ll=mergeSort(left)
    rl=mergeSort(right)
    return merge(ll,rl)
def merge(left, right):
    result = []
    i = j = 0
    while len(left) > i and len(right)>j:
        if left[i] <=right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__=="__main__":
    li=[3,2,5,6,9,4]
    l2=mergeSort(li)
    print(l2)
    li2=[3,4,5,2]
    print(mergeSort(li2))
#    """先从简单的理解 复杂的是一样的"""
"""https://www.cnblogs.com/bianjing/p/10260264.html"""
"""https://www.cnblogs.com/b02330224/p/9201293.html"""