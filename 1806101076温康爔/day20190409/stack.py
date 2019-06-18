stack=[]

#压栈
stack.append(1)
stack.append(2)
stack.append(3)

#出栈
print(stack.pop())    #输出：3
print(stack.pop())    #输出：2
print(stack.pop())    #输出：1

for i in range(1, 10):
    stack.append(i)

#当栈不为空时
while len(stack) is not 0:
    print(stack.pop())
