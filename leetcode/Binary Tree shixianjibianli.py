# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:09:47 2019

@author: Administrator
"""

"""二叉树实现以及遍历"""
class Node():
    def __init__(self,item):
        self.item=item
        self.lchild=None
        self.rchild=None
class Tree():
    def __init__(self):
        self.root=None
    def add(self,item):
        node=Node(item)
        if self.root==None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            cur_node=queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild=node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild=node
                return
            else:
                queue.append(cur_node.rchild)
    """层次遍历(队列）"""               
    def bfs(self):
        if self.root==None:
            return
        queue=[self.root]
        while queue:
            cur_node=queue.pop(0)
            print(cur_node.item,end='')
            if cur_node.lchild !=None:
                queue.append(cur_node.lchild)
            if cur_node.rchild !=None:
                queue.append(cur_node.rchild)
    """前中后遍历（递归）"""
    def pre_travel(self,node):
        if node is None:
            return
        print(node.item,end='')
        self.pre_travel(node.lchild)
        self.pre_travel(node.rchild)
    def mid_travel(self,node):
        if node is None:
            return
        self.mid_travel(node.lchild)
        print(node.item,end='')
        self.mid_travel(node.rchild)
    def post_travel(self,node):
        if node is None:
            return
        self.post_travel(node.lchild)
        self.post_travel(node.rchild)
        print(node.item, end="")
if __name__=="__main__":
    tree=Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.bfs()
    print(" ")
    tree.pre_travel(tree.root)
    print(" ")
    tree.mid_travel(tree.root)
    print(" ")
    tree.post_travel(tree.root)
"""https://blog.51cto.com/10777193/2395373"""
"""深度优先还有迭代的写法 这里暂时按下不表"""

"""第二种"""
#class BiTreeNode():
#    def __init__(self,data):
#        self.data=data
#        self.lchild=None
#        self.rchild=None
#a = BiTreeNode('A')
#b = BiTreeNode('B')
#c = BiTreeNode('C')
#d = BiTreeNode('D')
#e = BiTreeNode('E')
#f = BiTreeNode('F')
#g = BiTreeNode('G')
#e.lchild = a
#e.rchild = g
#a.rchild = c
#c.lchild = b
#c.rchild = d
#g.rchild = f
#root=e
#def pre_order(root):
#    if root:
#        print(root.data,end='')
#        pre_order(root.lchild)
#        pre_order(root.rchild)
#pre_order(root)

            
                        
            