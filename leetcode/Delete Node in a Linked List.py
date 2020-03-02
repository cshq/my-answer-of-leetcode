# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:37:22 2019

@author: THTF
"""


def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val=node.next.val
    node.next=node.next.next