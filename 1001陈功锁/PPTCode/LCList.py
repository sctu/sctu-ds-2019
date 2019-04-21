from LNode import LNode

class LCList: # class of Circular Linked List
    def __init__(self):
        self.rear = None
        
    def isEmpty(self):
        return self.rear is None
    
    def prepend(self, elem): # add element in the front end
        p = LNode(elem, None)
        if self.rear is None:
            p.next = p # initiates circle
            self.rear = p
        else:
            p.next = self.rear.next
            self.rear.next = p
            
    def append(self, elem): # add element in the rear end
        self.prepend(elem)
        self.rear = self.rear.next
        
    def pop(self): # pop out head element
        if self.rear is None:
            raise ValueError
        p = self.rear.next
        if self.rear is p:
            self.rear = None
        else:
            self.rear.next = p.next
        return p.elem
    
    def printall(self):
        p = self.rear.next
        while True:
            print(p.elem)
            if p is self.rear:
                break
            p = p.next

if __name__ == '__main__':
    mlist = LCList()
    for i in range(10):
        mlist.prepend(i)
    for i in range(11, 20):
        mlist.append(i)
    #mlist1.printall()

    while not mlist.isEmpty():
        print(mlist.pop())

