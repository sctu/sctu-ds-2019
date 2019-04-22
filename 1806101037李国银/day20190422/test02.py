# coding: utf-8

# 结点类
class Node:

    # 类有两个属性：data  和next
    def __init__(self,data):
        self.data =data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# node1的下一个是node2
node1.next = node2

# node2的下一个是node3
node2.next = node3