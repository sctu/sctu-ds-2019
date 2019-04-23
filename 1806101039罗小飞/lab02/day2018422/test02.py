# coding:utf-8
# 节点类


class Node:
    # 类有两个属性：date和next
    def __init__(self, date):
        self.date = date
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(3)
node5 = Node(3)
node6 = Node(3)
node7 = Node(3)
node8 = Node(3)



# node1的后面是node2，node2的后面是node3
node1.next = node2
node2.next = node3


# 只知道第一个节点的值如何打印Node链中的所有元素

node = node1
while node is not None:
    print(node.date)
    node = node.next
# def add(a,b):
#     return a+b
#
#
# print(add(1, 2))
