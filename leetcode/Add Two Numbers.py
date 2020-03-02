# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:03:48 2019

@author: THTF
"""
class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1,l2):
    l3=ListNode(0)
    carry=0
    pre=l3
    while l1 or l2:
#        需要是or
        x=l1.val if l1 else 0
#        防止l1为空的情况下，报错
        y=l2.val if l2 else 0
        l3.next=ListNode((x+y+carry)%10)
#        不能漏掉carry
        carry=1 if (x+y+carry)>=10 else 0
        l3=l3.next
#        下面要有个判断
        if l1!=None:
            l1=l1.next
        if l2!=None:
            l2=l2.next
    if carry==1:
        l3.next=ListNode(1)
    return pre.next