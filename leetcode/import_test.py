# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 23:02:01 2019

@author: THTF
"""

import water_fall as wp
wf_test=wp.water_fall([900,1245,1638,1530,1376,1511,1689,1975,1856,1495,1292])
a=wf_test.sup_col()
b=wf_test.postive_add()
c=wf_test.negative_add()
#    print(wf_test.data)
print(a) 
print(b)
print(c)