# 10个结点的单链表，值为1，2，...，10

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# 头结点(尾插法)
head = Node(-1)
tail = head

for i in range(1, 11):

    # (1) 创建一个新的结点
    new_node = Node(i)

    # (2) 将当前等链表的最后一个结点（尾结点）
    tail.next = new_node

    # (3) 更新尾结点的值
    tail = new_node





