class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        #头结点
        self.head = Node(-1)

        #4.第i个节点前插入值为value的节点
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

if __name__ == 'main':
    my_list = List()

    my_list.list_element_add(3, 10)
    my_list.list_print()