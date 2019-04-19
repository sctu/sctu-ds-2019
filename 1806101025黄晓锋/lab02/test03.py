#回文判断
stack=[]
queue=[]

X=input('请输入一段文字：')

n=len(X)
if n%2==0:
    m=n/2
    for m in X:
        stack.append(m)
else :
    m=(n+1)/2
    for m in X:
        stack.append(m)
    print(stack)