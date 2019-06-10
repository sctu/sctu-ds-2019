class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class List:

    def __init__(self):
        # 头节点
        self.head = Node(-1)

# 清空链表
    def list_clear(self):
        self.head.next = None