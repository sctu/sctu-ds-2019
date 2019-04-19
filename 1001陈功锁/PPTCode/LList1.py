from LNode import LNode
from LList import LList

class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self.rear = None
        
    def prepend(self, elem):
        self.head = LNode(elem, self.head)
        if self.rear is None: # empty list
            self.rear = self.head
            
    def append(self, elem):
        if self.rear is None: # empty list
            self.prepend(elem)
        else:
            self.rear.next = LNode(elem, None)
            self.rear = self.rear.next
            
    def pop(self):
        if self.head is None:
            raise ValueError
        e = self.head.elem
        if self.rear is self.head: # list with one node
            self.rear = None
        self.head = self.head.next
        return e
    
    def poplast(self):
        return None # to be implemented

if __name__ == '__main__':
    mlist1 = LList1()
    for i in range(10):
        mlist1.prepend(i)
        
    for i in range(11, 20):
        mlist1.append(i)
        
    mlist1.printall()

