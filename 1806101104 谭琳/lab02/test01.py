print('hello')
#压栈操作是append()
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
#ctrl+d复制一行
#ctrl+s删除一行
#出栈的操作是pop（）
print(stack.pop())
print(stack.pop())
print(stack.pop())

for i in range(1,11):
    stack.append(i)
    #ctrl+/快速注释
while len(stack)!=0:
    print(stack.pop())


for i in range('hello,world'):
    stack.append(i)
while len(stack)!=0:

