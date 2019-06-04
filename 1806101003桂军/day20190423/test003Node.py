#10个结点的单链表，值为1，2,，3，.....，10
class Node:
    def __init__(self,date):
        self.data = date
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
# ...
n10 = Node(10)

n1.next = n2
n2.next = n3
# ...
