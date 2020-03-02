# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:08:29 2019

@author: Administrator
"""

"""二叉树的最小深度Minimum Depth of Binary Tree
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2."""
def minDepth(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        # 如果当前非空节点的左子树为None，而右子树不为None，说明得在右子树中找叶子结点
        if root.left is None and root.right is not None:
            return self.minDepth(root.right)+1
        # 如果当前非空节点的左子树不为None，而右子树为None，说明得在左子树中找叶子结点
        elif root.left is not None and root.right is None:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
    
"""很多人写出的代码都不符合 1,2 这个测试用例，是因为没搞清楚题意

题目中说明:叶子节点是指没有子节点的节点，这句话的意思是 1 不是叶子节点

题目问的是到叶子节点的最短距离，所以所有返回结果为 1 当然不是这个结果

另外这道题的关键是搞清楚递归结束条件

叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
当 root 节点左右孩子都为空时，返回 1
当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值"""