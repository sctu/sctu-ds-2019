# 10�����ĵ�����ֵΪ1,2,...��10
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
# ...
n10 = Node(10)

n1.next = n2
n2.next = n3
# ...



