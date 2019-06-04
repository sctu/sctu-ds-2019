#创建一个类
class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

#表达节点间的关系
node1.next = node2
node2.next = node3
node3.next = None

'''
用python实现列表的操作思路
创建一个一个的单列表
链接一个个的节点
'''