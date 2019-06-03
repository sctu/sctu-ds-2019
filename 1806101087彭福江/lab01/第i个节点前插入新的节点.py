#第i个节点前插入值为value的节点
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
