stack=[]
#压栈
stack.append(1)
stack.append(2)
stack.append(3)
for i in range(1, 11):
    stack.append(i)
#clrl+d  复制光标所在行的代码
#clrl+x  剪切光标所在行的代码
#出栈
#1、出栈次数为列表的长度
n=len(stack)
for i in range(n):
    a=stack.pop()
    print(a)
#2、当栈不为空时，一直出栈
while len(stack)is not 0:
    c=stack.pop()
    print(c)

#a=stack.pop()
#print(a)





