#单链表实现
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

for i in range(1,11):
    name = 'n' + str(i)
    data=locals()['n' + str(i)] = i

    print(name,data)