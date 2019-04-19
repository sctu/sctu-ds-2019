stack = []

# 压栈
stack.append(1)
stack.append(2)
stack.append(3)
#...
stack.append(10)

for i in range(1,11):
    stack.append(i)

#ctrl+D 复制粘贴一行
#ctrl+x  删除一行

a=stack.pop()
print(a)

for i in 'hello':
    print(i)

#当栈不为空的时候，一直pop()
while len(stack) is not 0:
    a = stack.pop()
    print(a)

s='hello word!'
r=s[::-1]
print(r)]

