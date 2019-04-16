stack = []

stack.append(1)
stack.append(2)
stack.append(3)

#ctrl+df复制前项
#ctrl+x剪切代码
#ctrl+w多项选择

print(stack.pop())
print(stack.pop())
print(stack.pop())

while len(stack) is not 0:
    print(stack.pop())