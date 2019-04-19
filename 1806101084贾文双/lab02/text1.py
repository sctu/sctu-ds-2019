class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

for i in range(10):
    node = Node(i)

node1.next = node2
node2.next = node3
node3.next = None


