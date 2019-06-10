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

        if __name__ == '__main__':
            my_list = List()

            my_list.insert_before([1, 2, 3, 4, 5])
            my_list.list_print()

        def list_print(self):
            node = self.head.next

            while node:
                print(node.value)
                node = node.next