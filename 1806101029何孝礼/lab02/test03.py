list=[]
def a(s):
    for i in s:
        list.append(i)
    list1=list.copy()
    list2=[]
    while len(list)!=0:
        list2.append(list.pop())
    if list2==list1:
        return True
    else:
        return False
print(a("abcdcba"))