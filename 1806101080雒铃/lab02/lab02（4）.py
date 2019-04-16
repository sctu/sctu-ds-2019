#创建两个栈
arr=[]
l=[]
#入栈，将第一个全部数分别压入两个栈中
while True:
    n=eval(input())
    arr.append(n)
    if len(l)==0:
        l.append(n)
#之后入栈，直接压入arr，列表l中判断前一个是否大于后一个
#如果前者大则返回最小值为后者，且后者压栈到列表l
    else:
        if l[-1]>=n:
            l.append(n)
# 如果前者大则返回最小值为前者，且将最小值压栈
        else:
            x=l[-1]
            l.append(x)
    print(l[-1])