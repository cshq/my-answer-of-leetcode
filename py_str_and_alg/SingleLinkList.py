# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:50:55 2019

@author: Administrator
"""

class Node():
    def __init__(self,elem):
        self.elem=elem
        self.next=None
class SingleLinkList():
    def __init__(self,node=None):
        self._head=node
    def is_empty(self):
        return self._head==None
    def length(self):
        cur=self._head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    def travle(self):
        cur=self._head
        while cur!=None:
            print(cur.elem)
            cur=cur.next
    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self._head=node
        else:
            cur=self._head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

if __name__=="__main__":
    ll=SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    
    ll.append(1)
    print(ll.is_empty())
    print(ll.length()) 
    
    ll.append(2)
    ll.append(5)
    ll.append(8)
    print(ll.length())
    ll.travle()

        
       


    
        