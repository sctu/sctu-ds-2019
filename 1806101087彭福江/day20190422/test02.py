"chen",18,"male"
#类的首字母是大写
#结点类
class Node:


    def __init__(self,date):
        self.date = date
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

#node1的下一个是node2
node1.next = node2
#node2的下一个是node3
node2.next = node3
#如何打印单链表的所有节点的数据
print(node1.date)
print(node2.date)
print(node3.date)

node = node1

node = node.next
while node is not None:
    print(node.date)

    node = node.next