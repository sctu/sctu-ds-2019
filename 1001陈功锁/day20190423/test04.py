# coding: utf-8

# 10个结点的单链表，值为1,2,...，10
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(-1)
tail = head

# 尾插法创建单链表
for i in range(1, 11):
    # (1) 创建一个新的结点
    new_node = Node(i)

    # (2) 将当前链表的最后一个结点(尾结点)
    # 的next设置为新节点
    tail.next = new_node

    # (3) 更新尾结点的值
    tail = new_node

# 打印单链表
node = head.next
while node is not None:
    print(node.data)
    node = node.next










