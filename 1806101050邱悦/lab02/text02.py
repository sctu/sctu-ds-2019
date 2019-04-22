kh={'}':'{',']':'[',')':'('}
n=input()
def check(n):
    arr=[]
    for i in n:
        if i in kh.values():
            arr.append(i)
        elif i in kh.keys():
            if arr and arr[-1]==kh[i]:
                arr.pop()
            else:
                return False
    return not arr
print(check(n))