stack = []

# 压栈
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
# ...
stack.append(10)

for i in range(1, 11):
    stack.append(i)

# for i in 'hello':
#     print(i)


# ctrl + d
# ctrl + x
a = stack.pop()
print(a)

# 代码重复
# 当栈不为空的时候，一直pop()
while len(stack) is not 0:
    a = stack.pop()
    print(a)
