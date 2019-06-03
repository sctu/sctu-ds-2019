class Node:
    def __init__(self,date):
        self.data=data
        self.next=Node
#尾插法
head = Node(-1)
#定义变量
tail = head
#n1 = Node(1)
#head.next = n1

for i in range(1,11):
    #创建一个新的节点
    new_node = Node(1)
#将当前链表的最后一个节点（尾节点）的next设置为新节点
# 将当前链表的最后一个节点修改为新创建的节点
    tail.node= new_node
    #更新尾节点的值
    tail = new_code



    #前插法：将头结点的next修改为新的节点