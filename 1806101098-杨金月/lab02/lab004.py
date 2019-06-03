arr=[]
l=[]
while True:
    n=eval(input())
    arr.append(n)
    if len(l)==0:
        l.append(n)
    else:
        if l[-1]>=n:
            l.append(n)
        else:
            x=l[-1]
            l.append(x)
    print(l[-1])