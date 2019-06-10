class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class List:
    def __init__(self):

        self.head = Node(-1)

    def insert_before(self,data):
        for i in data:
            node = Node(i)

            if self.head.next is None:
                self.head.next = node
            else:
                node.next = self.head.next
                self.head.next = node


if __name__== '_main_':
    my_list = List()
