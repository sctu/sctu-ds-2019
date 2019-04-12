

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())

#当栈不为空的时候一直pop
while len(stack) is not 0:
    a=stack.pop()
    print(a)


    print('hello')