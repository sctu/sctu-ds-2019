stack=[]
# 压栈
# ctrl+d  复制一行
# ctrl+x  剪切一行
#a=stack.pop()
#print(a)
for i in range(1,11):
    stack.append(i)
for i in range(1,11):
    a=stack.pop()
    print(a)
while len(stack) is not 0:
    c=stack.pop()
    print(c)




