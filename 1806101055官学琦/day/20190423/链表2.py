class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=None
#创建一个头部节点,尾插法
head=Node(-1)
tail=head

for i in range(10):
    x=input()
    new_node=Node(x)
    tail.next=new_node
    tail=new_node
#头插法
for j in range(10):
    y=input()
    new_node2=Node(y)
    tail.next