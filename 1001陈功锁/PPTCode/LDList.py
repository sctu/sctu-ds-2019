from LNode import LNode
from LList1 import LList1

class LDNode(LNode): # class of Double Linked Nodes
    def __init__(self, prev, elem, nxt):
        LNode.__init__(self, elem, nxt)
        self.prev = prev

class LDList(LList1): # class of Double Linked List
    def __init__(self):
        LList1.__init__(self)
        
    def prepend(self, elem):
        p = LDNode(None, elem, self.head)
        self.head = p
        if self.rear is None: # insert in empty list
            self.rear = p
        else: # otherwise, create the prev reference
            p.next.prev = p
            
    def append(self, elem):
        p = LDNode(self.rear, elem, None)
        self.rear = p
        if self.head is None: # insert in empty list
            self.head = p
        else: # otherwise, create the next reference
            p.prev.next = p
            
    def pop(self):
        if self.head is None:
            raise ValueError
        e = self.head.elem
        self.head = self.head.next
        if self.head is None:
            self.rear = None # it is empty now
        else:
            self.head.prev = None
        return e
    
    def poplast(self):
        if self.head is None:
            raise ValueError
        e = self.rear.elem
        self.rear = self.rear.prev
        if self.rear is None:
            self.head = None # it is empty now
        else:
            self.rear.next = None
        return e

if __name__ == '__main__':
    mlist = LDList()
    for i in range(10):
        mlist.prepend(i)
    for i in range(11, 20):
        mlist.append(i)
    #mlist1.printall()

    while not mlist.isEmpty():
        print(mlist.pop())
        if not mlist.isEmpty():
            print(mlist.poplast())


        

