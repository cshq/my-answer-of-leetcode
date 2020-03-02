# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:59:35 2019

@author: Administrator
"""

"""平衡二叉树Balanced Binary Tree
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。"""
def isBalanced(root):
    if root is None:
        return True
    # 分别定义左右子树的高度
    left_depth = 0
    right_depth = 0
    if root.left:
        left_depth = get_depth(root.left)
    if root.right:
        """以上两个判断也可以没有"""
        right_depth = get_depth(root.right)
    if abs(left_depth - right_depth) > 1:
        return False
    else:
        return isBalanced(root.left) and isBalanced(root.right)

# 获取某一节点对应树的最大高度
def get_depth(root):
    if root is None:
        return 0
    else:
        return max(get_depth(root.left), get_depth(root.right))+1
