# 10个结点的单链表，值为1，2，...，10

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# 头结点(尾插法)
head = Node(-1)
tail = head

for i in range(1, 11):

    # (1) 创建新的结点
    new_node = Node(i)

    # (2) 将当前等链表的最后一个结点（尾结点）
    # 设置新节点的next为头结点的next
    # 头结点每次都指向最后一个结点
    tail.next = new_node

    # (3) 更新尾结点的值
    tail = new_node

# 打印单链表
node = head.next
while node is not None:
    print(node.data)
    node = node.next






