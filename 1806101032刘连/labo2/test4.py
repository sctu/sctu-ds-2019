a=[]
b=[]
while True:
    m=eval(input())
    a.append(m)
    if len(b)==0:
        b.append(m)
    else:
        if b[-1]>=m:
            b.append(m)
        else:
            n=b[-1]
            b.append(n)
    print(b[-1])