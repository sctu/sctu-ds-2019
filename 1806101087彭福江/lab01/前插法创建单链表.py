class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class List:

    def __init__(self):
        #头节点
        self.head = Node(-1)

        #前插法创建单链表
        def insert_before(self,data):
            for i in data:
                node = Node(i)

                if self.head.next is None:
                    self.head.next = node
                else:
                    node.head.next = node