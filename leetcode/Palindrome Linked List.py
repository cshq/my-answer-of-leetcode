# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:34:38 2019

@author: THTF
"""


def isPalindrome(head):
    slow=head
    fast=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    if fast:
        slow=slow.next
#取中点
    pre=None
    cur=slow
    while cur:
        tmp=cur.next
        cur.next=pre
        pre=cur
        cur=tmp
#调换
    while pre and head:
        if pre.val!=head.val:
            return False
        pre=pre.next
        head=head.next
    return True
#判段