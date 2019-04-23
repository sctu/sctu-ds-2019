l=input()
a=[]
b=[]
for i in l:
    a.append(i)
for j in range(1,len(l)+1):
    b.append(l[-j])
if a==b:
    print(True）
    else:
    print(False)