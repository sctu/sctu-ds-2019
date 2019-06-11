# 打印单链表
def list_print(self):
    node = self.head.next

    while node:
        print(node.value)
        node = node.next

if __name__== '_main_':
    my_list = List()

    my_list.insert_before([1, 2, 3, 4, 5])


    my_list.list_clear ()

    my_list.insert_tail([1, 2, 3, 4, 5])
    my_list.list_print()

    my_list.list_element_add(3, 10)
    my_list.list_print()
