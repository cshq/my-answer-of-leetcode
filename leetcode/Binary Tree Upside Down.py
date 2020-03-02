# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:15:44 2019

@author: Administrator
"""
"""	上下翻转二叉树
Binary Tree Upside Down"""
"""solution1 :递归"""
def upsideDownBinary(root):
    if not root or not root.left:
        return root
    newroot=upsideDownBinary(root.left)
    root.left.left=root.right
    root.left.right=root
    root.left=None
    root.right=None
    return newroot

"""https://segmentfault.com/a/1190000016755610"""

"""solution2:迭代"""