# 10各结点的单链表，值为1，2，……9，10
class Node:

    def __init__(self,data,next):
        self.data = data
        self.next = None

head = Node(-1)

for i in range(1,11):
    # (1) 创建一个新的结点
    new_node = Node(i)

    # (2) 将当前链表的最后一个结点（尾结点）的next设置为新结点
    tail.next = new_node

    # (3) 更新为结点的值
    tail = new_node

node = head.next
while node is not None:
    print(node.data)
    node = node.next
