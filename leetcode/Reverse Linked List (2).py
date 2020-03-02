# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:54:27 2019

@author: Administrator
"""
"""反转链表 Reverse Linked List
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL"""

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    new_head=None
    while head:
        tmp=head.next
        """保存head的后置节点"""
        head.next=new_head
        """head指向new_head"""
        new_head=head
        """new_head更新为现在的head（这一步很关键，容易漏掉或者想不到）"""
        head=tmp
        """head更新为tmp"""
    return new_head