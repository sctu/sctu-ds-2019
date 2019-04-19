stack=[]
#压栈
'''
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
#.......
stack.append(10)
a=stack.pop()
'''
#代码重复
#当栈不为空的时候，一直pop(）
'''
while len(stack) is not 0:
    a=stack.pop()
    print(a)
for i in range(1,11):
    stack.append(i)
'''
#cral+d 复制一行  +x删除一行
'''
for i in "Hello World!":
    stack.append(i)
while len(stack) is not 0:
    a=stack.pop()
    print(a)

for i in "Hello world!":
    stack.append(i)
while len(stack) is not 0:
    a=stack.pop()
    print(a)

