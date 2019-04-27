a=input()
stack=[]
l=[]
x=[]
w=[]
j=[]
k=[]
for i in a:
    l.append(i)
for n in a:
    x.append(n)
    a1=x.pop()
    w.append(a1)
    a2=w.pop()
    k.append(a2)

if l==k:
    print("True")
else:
    print("wrong")