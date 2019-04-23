#1、抽象一个节点类
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = None#使得next为空。

#2、有三个节点
   #三个节点的变量信息
n1 = Node(1)
n2 = Node(2)

n3 = Node(3)
#3、表达每一个节点之间的关系
   #n1的下一个节点为n2
n1.next = n2

   #n2的下一个节点为n3
n2.next = n3