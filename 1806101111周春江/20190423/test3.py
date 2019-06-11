class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = Node(-1)
tail = head
for i in range(1,11):

    #(1)创建一个新的结点
    new_node = Node(i)

    #(2)将当前列表的最后一个结点（尾结点）的next设置为新节点
    tail.next = new_node

    #3)更新尾节点的值
    tail = new_node
#2.有三个结点
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

#3.表达每一个结点之间的关系
# n1的下一个结点是n2
n1.next = n2
# n2的下一个结点是n3
n2.next = n3


