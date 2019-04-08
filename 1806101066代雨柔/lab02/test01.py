print("hello")
stack=[]
#1.压栈 push/python中的操作是append()
# stack.append(1)
# stack.append(2)
# stack.append(3)#c+D复制一行/c+x删除一行
#c+/ 快速注释以及反注释
for i in range(1,11):
    stack.append(i)

#2.出栈/python中的操作是pop()
print(stack.pop())
print(stack.pop())
print(stack.pop())

while len(stack)!=0:
    print(stack.pop())


stack=[]
for i in "hello,world":
    stack.append(i)
result=[]
while len(stack) is not 0:
    result.append(stack.pop())
print(result)




