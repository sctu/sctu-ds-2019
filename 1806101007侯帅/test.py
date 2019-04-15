

stack=[]
for i in 'hello,world!':
    stack.append(i)


result=[]
while len(stack)is not 0:
    result.append(stack.pop())

print(''.join(result))

#ctrl+d 复制上一行
#ctrl+w  扩展选择