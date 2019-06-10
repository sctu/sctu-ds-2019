class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class List:

    def __init__(self):
        # 头节点
        self.head = Node(-1)

# 打印单链表
    def list_print(self):
        node = self.head.next

        while node:
            print(node.value)
            node = node.next
