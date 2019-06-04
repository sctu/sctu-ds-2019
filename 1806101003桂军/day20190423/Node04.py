class Node:
    def __init__(self,date):
        self.data = date
        self.next = None

head = Node(-1)
tail = head
#尾插法
for i in range(1,11):
    #创建一个新的结点
    new_node = Node(i)
    #将当前链表的最后一个结点（尾结点）的next设置为新结点
    tail.next = new_node
    #更新尾结点的值
    tail = new_node
 # 打印单链表
node = head.next
while node is not None:
    print(node.data)
    node = node.next