class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.head = Node(-1)

    def insert_before(self, date):
        for i in date:
            node = Node(i)

            if self.head.next is None:
                self.head.next = node
            else:
                node.next = self.head.next
                self.head.next = node

    def insert_tail(self, date):

        tail = self.head.next
        for i in date:
            node = Node(i)
            if tail is None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node

    def list_print(self):
        node = self.head.next

        while node:
            print(node.value)
            node = node.next

    def list_clear(self):
        self.head.next = None

    def list_element_add(self, i, value):
        node_new = Node(value)
        index = 0
        node = self.head.next
        while node:
            index = index + 1
            if index == i-1:
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
