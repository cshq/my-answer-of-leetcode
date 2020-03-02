# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:36:10 2019

@author: THTF
"""

def lowestCommonAncestor(root,p, q):
        if (root.val-p.val)*(root.val-q.val)<=0:
            return root
        if p.val<root.val and q.val<root.val:
            return lowestCommonAncestor(root.left,p,q)
        if p.val>root.val and q.val>root.val:
            return lowestCommonAncestor(root.right,p,q)