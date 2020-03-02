# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:14:26 2019

@author: THTF
"""
def reverseVowels(s):
    arr = list(s)
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    p1, p2 = 0, len(arr) - 1
    while p1 < p2:
        while arr[p1] not in vowel:
            if p1<p2:
                
                p1 += 1
            else:
                break
#            类似下面的，可以直接p1<p2放到循环条件里
        while arr[p2] not in vowel and p1 < p2:
            p2 -= 1
        if p1 < p2:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 -= 1
    return ''.join(arr)