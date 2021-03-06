class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(-1)

# 前插法创建单链表
for i in range(1, 11):
    # (1) 创建新的结点
    new_node = Node(i)

    # (2) 设置新节点的next为头结点的next
    # 头结点每次都指向最后一个结点
    new_node.next = head.next

    # (3) 更新头结点的值
    head.next = new_node

# 打印单链表
node = head.next
while node is not None:
    print(node.data)
    node = node.next

