class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)

n1.next = n2
n2.next = n3
#.....
n10.next = n10
 #3.表达的是每一个结点之间的关系
#n1的下一个结点是n2
n1.next = n2

#n2的下一个结点是n3
n3.next = n3
