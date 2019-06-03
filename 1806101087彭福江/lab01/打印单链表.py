#打印单链表
def list_print(self):
    node = self.head.next

    while node:
        print(node.value)
        node = node.next