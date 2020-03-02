# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:27:17 2019

@author: Administrator
"""

class MinStack():
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    def push(self,x):
        self.stack.append(x)
        if not self.min_stack  or x<=self.min_stack[-1]:
            self.min_stack.append(x)
    def pop(self):
        if self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
    

        
if __name__=="__main__":
    minStack=MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())

           