# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:08 2019

@author: Administrator
"""

"""合并两个有序链表Merge Two Sorted Lists
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4"""
"""solution1: iteration"""
class ListNode():
    def __init__(self,x):
        self.value=x
        self.next=None
def mergeTwoLists(l1,l2):
    if l1 is None and l2 is None:
        return None
    new_list=ListNode(0)
    pre=new_list
    while l1 and l2:
        if l1.val<l2.value:
            pre.next=l1
            l1=l1.next
        else:
            pre.next=l2
            l2=l2.next
        pre=pre.next
    pre.next=l1 if l1 is not None else l2
#注意为什么定义了new_list还要定义pre.       此题详解见leetcode官方解答
"""solution2 :recursion"""
def mergeTwolists2(l1,l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next =mergeTwolists2(l1.next, l2)
        return l1
    else:
        l2.next =mergeTwolists2(l1, l2.next)
        return l2
#此题详解见leetcode官方解答