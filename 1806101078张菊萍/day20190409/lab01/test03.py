n=input()
l=[]
x=[]
for i in n:
    l.append(i)
for j in range(1,len(n)+1):
    x.append(l[-j])
if l==x:
    print(True)
else:
    print(False)