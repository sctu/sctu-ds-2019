class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class List:
    def __init__(self):
        self.head=Node(-1)

    #前插法
    def insert_before(self,data):
        for i in data:
            node=Node(i)

            if self.head.next is None:
                self.head.next=node

    #尾插法
    def insert_tail(self,data):
        tail=self.head.next
        for i in data:
            node=Node(i)

            if tail is None:
                self.head.next=node
                tail=node
            else:
                tail.next=node
                tail=node
    #打印
    def list_print(self):
        node=self.head.next

        while node:
            print(node.value)
            node=node.next

    #清空链表
    def list_clear(self):
        self.head.next=None

    #在第i个节点前插值为value的节点
    def list_element_add(self, i, value):

        node_new = Node(value)

        index = 0

        node = self.head.next

        while node:
            index = index + 1

            if index == i - 1:
                break

            node = node.next

        if node is None:
            return False

        node_new.next = node.next
        node.next = node_new

if __name__ == '__main__':
    my_list = List()

    my_list.insert_before([1, 2, 3, 4, 5])
    my_list.list_print()

    my_list.list_clear()

    my_list.insert_tail([1, 2, 3, 4, 5])
    my_list.list_print()

    my_list.list_element_add(3, 10)

    my_list.list_print()
