
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)


for i in range(1, 11):
    stack.append(i)

# ctrl + d
# ctrl + x
# ctrl + w

result=[]


#当栈不为空时一直pop
while len(stack) != 0:
    print(stack.pop())




#ctrl+d 复制上一行
#ctrl+w  扩展选择