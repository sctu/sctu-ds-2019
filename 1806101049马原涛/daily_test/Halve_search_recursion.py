#二分查找
#递归版本
alist=[12,23,27,31,54,67,89,95,99]
def Halve_search(alist,item):
    n=len(alist)
    mid=n//2
    if n>0:
        if alist[mid]==item:
            return True
        elif alist[mid]>item:
            return Halve_search(alist[:mid],item)
        else:
            return Halve_search(alist[mid+1:],item)
    else:
        return False
print(Halve_search(alist,95))
print(Halve_search(alist,152))