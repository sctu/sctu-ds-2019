# coding: utf-8
# 结点类
class Node:
    # 类有,有两个属性:data next
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(1)
node4 = Node(4)
node2 = Node(2)
node5 = Node(5)
node3 = Node(3)

# node1的下一个是node4
node1.next = node4
# node4的下一个是node2
node4.next = node2
# node2的下一个是node5
node2.next = node5
# node5的下一个是node3
node5.next = node3
# node5的下一个是node3
# node5.next = node3

# 如何打印单链表的所有结点的数据

# node = node1
# print(node.data)
#
# # node = node1.next
# node = node.next

node = node1
while node is not None:
    print(node.data)

    node = node.next