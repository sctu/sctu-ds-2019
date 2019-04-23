class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

# n1的下一个结点是n2
n1.next = n2

# n2的下一个结点是n3
n2.next = n3