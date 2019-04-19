stack=[]

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

for i in range(1,11):
    stack.append(i)


#代码重复

#当栈不为空时，一直pop()
while len(stack) is not 0:
    a=stack.pop()
    print(a)

stack=[]

for i in 'Hello,world':
    stack.append(i)


while len(stack) is not 0:

    print (stack.pop())
