#1.抽象一个节点类
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#2.有三个节点
n1=Node(1)
n2=Node(2)
n3=Node(3)

#3.表达与下一个节点的关系
#n1的下一个节点是n2
n1.next=n2

#n2的下一个节点是n3
n2.next=n3