# 10个节点单链表，值为1，2，3，4，5，6，7，8，9，10
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = None

#头节点，首先他是一个节点，其次他是一个列表的头。
#头节点是不放数据的，通过头节点可以找到其他的节点。

head = Node(-1)
#有了一个头节点
tail = head#tail每次指向当前链表的最后一个节点。

#n1 = Node(1)
#head.next  = n1
#尾插法：每一次都在当前链表的后面插入一个新的节点。
#定义一个变量，每次都指向当前的最后一个节点。
  #1、定义变量tail
  #2、tail.next=new
  #3、tail=new

for i in range:
    # 1 创建一个新的节点使存在节点为i
    new_node = Node(i)
      #刚开始tail为空
      #头节点设置为第一个节点，尾节点设置为第一个节点。
    # 2 把当前链表的最后一个节点（尾节点）修改为新创建的节点（next设置为新节点）。
    tail.next = new_node
    # 3 尾节点变换（更新值）。
    tail = new_node