class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        #头结点
        self.head = Node(-1)

        #1.前插法创建单链表
        def insert_before(self,data):
            for i in data:
                node = Node(i)

                if self.head.next is None:
                   self.head.next = node
                else:
                   node.next = self.head.next
                   self.head.next = node

if __name__ == 'main':
    my_list = List()

    my_list.insert_before([1, 2, 3, 4, 5])
    my_list.list_print()



