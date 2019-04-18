stack=[]
for i in 'hello,world!': #将每个字符压栈
    stack.append(i)


result=[]



while len(stack)is not 0:

    result.append(stack.pop())

print(''.join(result))