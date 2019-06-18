'''实验一 链表的应用
一、实验目的和要求
（1）理解线性表的链式存储结构。

（2）熟练掌握动态链表结构及有关算法的设计。

（3）根据具体问题的需要，设计出合理的表示数据的链表结构，设计相关算法。

二、实验内容
1. 编程实现单链表的基本操作。

使用前插法创建单链表；
使用尾插法创建单链表；
打印单链表中的每一个元素。
第i个节点前插入新的节点。'''
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class List:

    def __init__(self):
        # 头节点
        self.head = Node(-1)

    # 前插法创建单链表
    def insert_before(self, data):
        for i in data:
            node = Node(i)

            if self.head.next is None:
                self.head.next = node
            else:
                node.next = self.head.next
                self.head.next = node

    # 尾插法创建单链表
    def insert_tail(self, data):

        tail = self.head.next

        for i in data:
            node = Node(i)

            if tail is None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node

    # 打印单链表
    def list_print(self):
        node = self.head.next

        while node:
            print(node.value)
            node = node.next

    # 清空链表
    def list_clear(self):
        self.head.next = None

    # 第i个节点前插入值为value的节点
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