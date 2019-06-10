class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class List:

    def __init__(self):
        # 头节点
        self.head = Node(-1)

# 尾插法创建单链表
    def insert_tail(self, data):

        tail = self.head.next

        for i in data:
            node = Node(i)

            if tail is None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node