# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:54:46 2019

@author: THTF
"""

def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    stack=[]
    path=path.split('/')
    for item in path:
        if item=='..':
            if stack:
                stack.pop()
        elif item=='.':
            continue
        elif item:
            stack.append(item)
#            elif item and item!='.':
#                stack.append(item)
#            这样也可以
    return '/'+'/'.join(stack)