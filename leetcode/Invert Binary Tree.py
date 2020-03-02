# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:30:11 2019

@author: THTF
"""


def invertTree(root):
    if not root:
        return None
    root.left,root.right=root.right,root.left
    root.left=invertTree(root.left)
    root.right=invertTree(root.right)
    return root