'''stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
for i in range(1,11):
    stack.append(i)
#ctrl+d  复制上一行到下一行
#ctrl+x  撤回
a=stack.pop()
print(a)'''

stack=[]
for i in "Hello,World!":
    stack.append(i)

str1=[]
while len(stack) is not 0:
    str1.append(stack.pop())
print("".join(str1))

