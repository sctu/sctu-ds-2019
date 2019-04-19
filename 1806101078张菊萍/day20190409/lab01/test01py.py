stack=[]
for i in 'hello world':
    stack.append(i)
print(stack)
while len(stack)!=0:
    print(stack.pop())