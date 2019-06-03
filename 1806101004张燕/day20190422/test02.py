# -*- coding: UTF-8 -*-
# 结点类
#1、定义类名字 class 类名
#类名一般首字母大写


class  Node:

    #类有两个属性：data和next
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

#node1的下一个是node2
node1.next = node4
#node2的下一个是node3
node2.next = node5
#node3的下一个是node
node4.next = node2
node5.next = node3



