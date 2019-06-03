# coding: utf-8


#结点类
class Node:

    #类有两个属性：data 和 next
    def __init__(self,data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

#node1的下一个是node2
node1.next = node2
node2.next = node3
#只告诉你第一个结点的变量node1
#如何打印单链表的所有结点的数据。
#node = node1
#print(node.data)      #第一个结点的值
#node = node1.next
#node = node.next



node = node1


while node is not Node:
    print(node.data)

    node = node.next
