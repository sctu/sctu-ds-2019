#二分查找

alist=[12,23,27,31,54,67,89,95,99]
def Halve_search(alist,item):
    n=len(alist)
    start=0
    end=n-1

    while start<=end:
        mid = (start + end) // 2
        if alist[mid]==item:
            return True
        elif item<alist[mid]:
            end=mid-1
        else:
            start=mid+1
    return False
print(Halve_search(alist,95))
print(Halve_search(alist,152))