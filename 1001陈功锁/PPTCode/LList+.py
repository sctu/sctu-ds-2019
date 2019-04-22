from LNode import LNode

class LList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head is None
    
    def prepend(self, elem):
        self.head = LNode(elem, self.head)
        
    def pop(self):
        if self.head is None:
            raise ValueError
        e = self.head.elem
        self.head = self.head.next
        return e
    
    def append(self, elem):
        if self.head is None:
            self.head = LNode(elem, None)
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem, None)

    def poplast(self):
        if self.head is None: # empty list
            raise ValueError
        p = self.head
        if p.next is None: # list with only one element
            e = p.elem; self.head = None
            return e
        while p.next.next is not None: # till p.next be last node
            p = p.next
        e = p.next.elem; p.next = None
        return e

    def find(self, pred):
        p = self.head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
        return None
    
    def printall(self):
        p = self.head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    def rev(self):
        p = None
        while self.head is not None:
            q = self.head
            self.head = q.next
            q.next = p
            p = q
        self.head = p

    def sortm(self):
        if self.head is None:
            return
        crt = self.head.next
        while crt is not None:
            x, p = crt.elem, self.head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next

    def sort(self):
        if self.head is None:
            return
        last = self.head; crt = last.next
        while crt is not None:
            p = self.head; q = None
            while p is not crt and p.elem <= crt.elem:
                q = p; p = p.next
            if p is crt:
                last = crt
            else:
                last.next = crt.next
                crt.next = p
                if q is None:
                    self.head = crt
                else:
                    q.next = crt
            crt = last.next        
#end of class LList

def listSort(lst) :
    for i in range(1, len(lst)): # seg [0:0] is sorted
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x: # moving one by one
            lst[j] = lst[j-1]         # in reversed-order
            j -= 1
        lst[j] = x

import random

if __name__ == '__main__':
    mlist1 = LList()

    for i in range(10):
        mlist1.prepend(i)

    for i in range(11, 20):
        mlist1.append(i)

    mlist1.printall()
    for i in range(5):
        print(mlist1.pop())
        print(mlist1.poplast())

    print('remained:')
    mlist1.printall()
    mlist1.rev()
    print('\nreversed:')
    mlist1.printall()

    mlist1.sort()
    print('\nsorted:')
    mlist1.printall()
    

##    list1 = [random.randint(1, 50) for i in range(20)]
##    print(list1, '\n')
##    listSort(list1)
##    print(list1)

