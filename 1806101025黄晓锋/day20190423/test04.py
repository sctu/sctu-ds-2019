#10个节点的单链表，值为：1，2，3......

#尾插
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
head=Node(-1)
tail=head

for i in range(1,11):
    #（1）创建一个新的节点
    new_node=Node(i)

    #（2）将当前链表的最后一个节点（尾节点）的next设置为新节点
    tail.next=new_node

    #（3）更新尾节点的值
    tail=new_node
'''