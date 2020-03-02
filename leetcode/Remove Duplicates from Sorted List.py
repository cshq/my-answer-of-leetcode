# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:41:41 2019

@author: Administrator
"""

"""删除排序链表中的重复元素Remove Duplicates from Sorted List
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2
示例 2:
输入: 1->1->2->3->3
输出: 1->2->3"""
class Node():
    def __init__(self,x):
        self.value=x
        self.next=None
def deleteDuplicates(head):
    cur=head
    if not cur:
        return None
    while cur.next:
        if cur.next.value==cur.value:
            cur.next=cur.next.next
        else:
            cur=cur.next
    return head
        
if __name__=="__main__":
    n1=Node(1)
    n2=n1.next=Node(1)
    n3=n2.next=Node(2)
    n4=n3.next=Node(3)
    n5=n4.next=Node(3)
    deleteDuplicates(n1)
    print(n1.next.value)