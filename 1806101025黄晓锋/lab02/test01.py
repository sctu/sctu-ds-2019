#反转
stack=[]
stack1=input("需要反转的字符串")

for i in stack1:
    stack.append(i)

n=len(stack)
for i in range(n):
    a=stack.pop()
    print(a,end='')