stack1=[]
stack2=[]
while  True:
    n=eval(input())
    stack1.append(n)
    if len(stack2) == 0:
        stack2.append(n)
    else:
        if stack2 [-1]>=n:
            stack2 .append(n)
        else:
            x = stack2 [-1]
            stack2 .append(x)
    print(stack2[-1])