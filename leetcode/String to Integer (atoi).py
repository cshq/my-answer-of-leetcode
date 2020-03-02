# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:40:29 2019

@author: THTF
"""

import re
def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    try:
        return max(min(int(re.search(r'^[+-]?\d+', str.lstrip()).group()),2**31-1),-2**31)
    except AttributeError:
        return 0