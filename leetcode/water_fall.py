# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:00:38 2019

@author: THTF
"""

class water_fall():
    def __init__(self,data=[]):
        self.data=data
    def sup_col(self):
        res=[0]*len(self.data)
        for i in range(1,len(self.data)):
            if self.data[i]-self.data[i-1]>0:
                res[i]=self.data[i-1]
            else:
                res[i]=self.data[i]
        return res
    def postive_add(self):
        res=['-']*len(self.data)
        res[0]=self.data[0]
        for i in range(1,len(self.data)):
            diff=self.data[i]-self.data[i-1]
            res[i]=diff if diff>=0 else '-'
        return res
    def negative_add(self):
        res=['-']*len(self.data)
        for i in range(1,len(self.data)):
            diff=self.data[i]-self.data[i-1]
            res[i]=abs(diff) if diff<0 else '-'
        return res
        
        
if __name__=='__main__':
    wf_test=water_fall()
    wf_test.data=[900,1245,1638,1530,1376,1511,1689,1975,1856,1495,1292]
    a=wf_test.sup_col()
    b=wf_test.postive_add()
    c=wf_test.negative_add()
    print(wf_test.data)
    print(a) 
    print(b)
    print(c)