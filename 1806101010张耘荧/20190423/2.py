class Node:
    def __init__(self,date):
        self.date = date
        self.next = None
head = Node(-1)
tail = head
for i in [0,10]:
    new_node = Node(i)
    tail.next = new_node
    tail = new_node




