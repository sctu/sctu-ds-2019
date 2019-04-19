from LCList import LCList

def JosephusA(n, k, m):
    people = list(range(1, n+1))
    num, i = 0, k-1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end = "")
                people[i] = 0
            i = (i+1) % n
        if num < n-1:
            print(", ", end="")
        else:
            print("")
    return

def JosephusL(n, k, m):
    people = list(range(1, n+1))
    if k < 1 or k > n:
        raise ValueError

    num, i = n, k-1
    for num in range(n, 0, -1):
        i = (i + m-1) % num            
        print(people.pop(i), end = "")
        if num > 1:
            print(", ", end="")
        else:
            print("")
    return

class Josephus(LCList):
    def turn(self, m):
        for i in range(m):
            self.rear = self.rear.next

    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        while not self.isEmpty():
            self.turn(m-1)
            print(self.pop(), end="")
            if not self.isEmpty():
                print(", ", end="")
            else:
                print("")
# end class Josephus

if __name__ == '__main__':
    s = input("Josephus parameters (n k m): ")
    n, k, m = map(int, s.split()) 
    JosephusA(n, k, m)    
    JosephusL(n, k, m)
    Josephus(n, k, m)

