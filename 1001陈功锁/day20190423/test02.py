# 1. ����һ�������
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# 2. ���������
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n = Node(4)

# 3. ���ÿһ�����֮��Ĺ�ϵ
# n1����һ�������n2
n1.next = n2

# n2����һ�������n3
n2.next = n3