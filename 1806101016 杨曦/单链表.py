 #10个结点的单链表，值为1,2,...，10
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

head = Node(-1)
tail = head
# 尾插法创建单链表
for i in range(1,11):
    #(1)创建了一个新结点
    new_node = Node(i)

    #(2)将当前链表的最后一个结点（尾结点）
    # 的next设置为新结点
    tail.next = new_node

    #(3)更新尾结点的值
    tail = new_node




#前插法创建单链表
    def insert_before(self,data):
        for i in data:
            node = Node(i)

            if self.head.next is None:
                self.head.next = node
            else:
                node.next = self.head.next
                self.head.next = node



# 打印单链表
node = head.next
while node is not None:
    print(node.data)
    node = node.next


#第i个节点前插入新的节点
def list_element_add(self, i, value):

    node_new = Node(value)
    index = 0
    node = self.head.next
    while node:
        index = index + 1
        if index == i - 1:
            break
        node = node.next

    if node is None:
        return False
    node_new.next = node.next
    node.next = node_new