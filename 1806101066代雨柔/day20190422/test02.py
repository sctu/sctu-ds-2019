# coding: utf-8
#结点类
class Node:
    #类两个属性data和next
    def __init__(self,data):
        self.data = data
        self.next =None
#node1表示变量的定义
node1=Node(1)#结点,‘1’对应data
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
#node1的next=node4
node1.next=node4
#node2的下一个是node5
node2.next=node5
#node4的下一个是node2
node4.next=node2
#node5的下一个是node3
node5.next=node3
#如何打印单链表的所有结点的数据
print(node1.data)
print(node2.data)
print(node3.data)
#只告诉第一个结点的变量node1，如何打印所有结点的值
node=node1
print(node.data)#第一个结点的值
#node=node1.next
node=node.next
while node is not None:
    print(node.data)

    node=node.next
