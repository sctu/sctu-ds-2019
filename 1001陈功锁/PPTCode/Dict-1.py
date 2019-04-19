""" Dictionary and searching 
"""

from Assoc import Assoc
from random import randint

# Suppose lst is a list of Assoc object,
# where e.key and e.value give their key and value respectively
def bisearch(lst, key):
    low, high = 0, len(lst)-1
    while low <= high: # There are elements in the interval
        mid = (low + high)//2
        if key == lst[mid].key:
            return lst[mid].value
        if key < lst[mid].key:
            high = mid - 1 # continue in the lower half part
        else:
            low = mid + 1  # continue in the higher half part

# A simple digit-str/general-str hash function
def int_str_hash(sn): 
    c = 0
    for c in sn:
        h = (h*10 + int(c)*31) % 65521
    return h

class LSet: # A part of a simple set class
    def __init__(self, elems = []):
        self.elems = []
        for x in elems:
            if x not in self.elems:
                self.elems.append(x)

    def includes(self, e):
        return e in self.elems
        
if __name__ == '__main__':

    lst1 = [Assoc(randint(1, 30), i) for i in range(16)]
    lst1.sort()
    print(list(map(str, lst1)))
    for i in range(1, 30, 3):
        ind = bisearch(lst1, i)
        print("Search", i, "in the list and get:", ind)

    pass
        
    

