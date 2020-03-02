# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:59:17 2019

@author: Administrator
"""

"""移除链表元素 Remove Linked List Elements。
删除链表中等于给定值 val 的所有节点
示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5"""
"""solution1"""
def removeElements(self, head, val):    
    if head==None:
        return None
    while head.val==val:
        head=head.next
        if head==None:
            return None
    newhead=head
    while head:
        if head.next and head.next.val==val:
            head.next=head.next.next
        else:
            head=head.next
    return newhead
"""solution2:递归"""

def removeElements2(head,val):
    if head==None:
        return
    else:
        if head.val==val:
            return removeElements(head.next, val)
        else:          
            head.next=removeElements(head.next,val)
            return head