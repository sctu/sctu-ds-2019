stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

for i in range(1,11):
    stack.append(i)
print(stack)
# 出栈
stack.pop(1)
stack.pop(4)
# 当栈不为空时一直pop
while len(stack) is not 0:
    print(stack.pop())
stack=[]

for i in 'hello,World!':
    stack.append(i)
result= []
while len(stack)is not 0:
    result.append(stack.pop())
print(''.join(result))
