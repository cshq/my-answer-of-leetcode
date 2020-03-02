# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 22:59:30 2019

@author: Administrator
"""


def josephus(n,m):
    jlist=list(range(n))
    while len(jlist)>1:
        for i in range(m-1):
            jlist.append(jlist.pop(0))
        jlist.pop(0)
    for i in jlist:
        print (i+1)
        

josephus(5,3)

 
 
