#定义栈
stack = []

#push
stack.append(1)
stack.append(2)
stack.append(3)

for i in range(1,11):
    stack.append(i)

#pop
print(stack.pop())

#pop一直到栈不为空
while len(stack) is not 0:
    print(stack.pop())