#单链表实现
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def infoamation(self):
        print(self.data,self.next)
headNode=Node(-1)
for i in range(1,11):
    name = 'n' + str(i)
    data=locals()['n' + str(i)] = i
    next='n'+str(i+1)
    name=Node(data,next)