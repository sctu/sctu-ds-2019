stack = []
#压栈
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)
stack.append(7)

for i in range(1, 11):
    stack.append(1)

for i in 'hello':
    print(i)
#ctrl+d  复制
#ctrl+x  删除

a = stack.pop()
print(a)

#代码重复
#当栈不为空的时候，一直pop（）
while len(stack) is not 0:
    a = stack.pop()
    print(a)