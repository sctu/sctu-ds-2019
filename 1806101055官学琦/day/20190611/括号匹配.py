kh={'}':'{',']':'[',')':'('}

n=input()

def check(n):
    ls = []
    for i in n:
        if i in kh.values():
            ls.append(i)
        elif i in kh.keys():
            if ls and ls[-1]==kh[i]:
                ls.pop()
            else:
                return False
    return not ls
print(check(n))