#stack=[]

#压栈append

#for i in range(1,11):
    #stack.append(i)


#ctrl+D 复制并粘贴所选内容
#ctrl+X 删除

#a=stack.pop()
#print(a)
#for i in  'hello':
    #print(i)
#while len(stack) is not 0:
    #a=stack.pop()
    #print(a)


stack=[]
a='hello world!'
for i in a:
    stack.append(i)

while len(stack) is not 0:
    print(stack.pop())