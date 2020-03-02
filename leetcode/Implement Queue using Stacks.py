# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:27:02 2019

@author: THTF
"""

import collections
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=collections.deque()
        self.stack_tmp=collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        for _ in range(len(self.stack)):
            self.stack_tmp.appendleft(self.stack.popleft())
        self.stack.appendleft(x)
        for _ in range(len(self.stack_tmp)):
            self.stack.appendleft(self.stack_tmp.popleft())
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.popleft()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack