stack = []

stack.append(1)
stack.append(2)
stack.append(3)


# ctrl + d
# ctrl + w
# ctrl + x

for i in range(1,11):
    stack.append(i)



print(stack.pop())
print(stack.pop())
print(stack.pop())


# 当栈不为空时一直pop
while len(stack) is not 0:
    print(stack.pop())




