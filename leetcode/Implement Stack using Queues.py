# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:31:27 2019

@author: THTF
"""
import collections
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        for _ in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.stack)