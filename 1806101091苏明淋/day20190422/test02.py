# coding: utf-8

# 结点类
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2

node2.next = node3

print(node1.data)
print(node2.data)
print(node3.data)


node = node1

while node is not None:
    print(node.data)

    node = node.next