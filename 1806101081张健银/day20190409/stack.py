# ctrl + d 复
#ctrl + x 删
#ctrl + w 选
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

for i in range(1,11):
    stack.append(i)


print(stack.pop())
print(stack.pop())
print(stack.pop())

#当栈不为空时一只pop
while len(stack) is not 0:
    print(stack.pop())