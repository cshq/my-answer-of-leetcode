# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:03:58 2019

@author: Administrator
"""

"""环形链表  Linked List Cycle
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例2
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。"""
"""solution1 :哈希"""
def hasCycle(head):
    s=set()
    if not head:
        return False
    while head:
        if head.next not in s:
            s.add(head.next)
            head=head.next
        else:
            return True
    return False
"""solution2: 快慢指针"""
"""设两指针fast slow指向链表头部head，迭代：
fast每轮走两步，slow每轮走一步，这样两指针每轮后距离+1;
若链表中存在环，fast和slow一定会在将来相遇（距离连续+1，没有跳跃）"""
def hasCycle2(head):
    slow,fast=head,head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return True
    return False