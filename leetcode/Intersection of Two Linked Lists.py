# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:56:09 2019

@author: Administrator
"""
"""相交链表:Intersection of Two Linked Lists"""
class LinkNode():
    def __init__(self,x):
        self.val=x
        self.next=None

headA=LinkNode(1)
headA.next=LinkNode(2)
headA.next.next=LinkNode(3)
headB=LinkNode(5)
headB.next=headA.next

"""solution1: 哈希"""
def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    hash_a={}
    while headA:
        hash_a[headA]=1
        headA=headA.next
    while headB:
        if headB in hash_a:
            return headB
        else:
            headB=headB.next
            
print(getIntersectionNode(headA,headB).val)

"""solution2 :O(1)空间复杂度"""
"""创建两个指针 pApA 和 pBpB，分别初始化为链表 A 和 B 的头结点。然后让它们向后逐结点遍历。
当 pApA 到达链表的尾部时，将它重定位到链表 B 的头结点 (你没看错，就是链表 B); 类似的，当 pBpB 到达链表的尾部时，
将它重定位到链表 A 的头结点。
若在某一时刻 pApA 和 pBpB 相遇，则 pApA/pBpB 为相交结点。
想弄清楚为什么这样可行, 可以考虑以下两个链表: A={1,3,5,7,9,11} 和 B={2,4,9,11}，相交于结点 9。
 由于 B.length (=4) < A.length (=6)，pBpB 比 pApA 少经过 22 个结点，会先到达尾部。将 pBpB 重定向到 A 的头结点，
 pApA 重定向到 B 的头结点后，pBpB 要比 pApA 多走 2 个结点。因此，它们会同时到达交点。
如果两个链表存在相交，它们末尾的结点必然相同。因此当 pApA/pBpB 到达链表结尾时，记录下链表 A/B 对应的元素。
若最后元素不相同，则两个链表不相交"""

def getIntersectionNode2(headA,headB):
        p,q=headA,headB
        while p!=q:
            p=p.next if p else headB
            q=q.next if q else headA
        return q

"""https://leetcode-cn.com/problems/intersection-of-two-linked-lists/"""
        
