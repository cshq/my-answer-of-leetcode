# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:33:39 2019

@author: THTF
"""

def reverseList(head):
    new_head = None
    
    while head :     
        tmp = head.next      # tmp这个变量名指向了head.next（也就是保存了head.next的地址）
        head.next = new_head  #head节点的下一个结点变为new_head
        new_head = head    #new_head这个变量名指向了head所指向（也可以说是保存，便于理解）的东西
        head = tmp   #head这个变量名指向了tmp（tmp在等号右边，所以和等号左边的tmp不一样 这里是实例化的tmp所指向的东西）
    
    return new_head

"""例： a=1  b=2  
a=b
这里右边的b就是实例化的2，表示a变量名指向了这个2，当然b也还是指向这个2的"""