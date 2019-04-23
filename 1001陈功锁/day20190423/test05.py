class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(-1)

# 前插法创建单链表
for i in range(1, 11):
    new_node = Node(i)
    new_node.next = head.next
    head.next = new_node

node = head.next
while node is not None:
    print(node.data)
    node = node.next

