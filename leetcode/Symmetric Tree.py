# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:45:31 2019

@author: Administrator
"""

"""对称二叉树 Symmetric Tree
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:如果你可以运用递归和迭代两种方法解决这个问题，会很加分。"""
def isSymmetric(root):
    if not root:
        return True
    return isMirror(root.left,root.right)
def isMirror(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False# 判断两棵树是否是镜像树
    if p.val!=q.val:
        return False
    return isMirror(p.left,q.right) and isMirror(p.right,q.left)
"""一棵树是否是对称树不能说子树是对称树,这要注意"""
