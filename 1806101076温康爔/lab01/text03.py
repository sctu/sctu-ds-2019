class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        #头结点
        self.head = Node(-1)

        # 3.打印单链表
        def list_print(self):
            noode = self.head.next

            while node:
                print(node.value)
                node = node.next

        # 3.清空链表
        def list_clear(self):
            self.head.next = None

if __name__ == 'main':
    my_list = List()

    my_list.list_clear()