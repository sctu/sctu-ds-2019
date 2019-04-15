stack=[]
#压栈
stack.append(1)
stack.append(2)
stack.append(3)
#crtl+d 复制
#crtl+x 剪切
a=stack.pop ()
print(a)

stack.append(1)
stack.append(2)
stack.append(3)
#...
stack.append(10)
for i in range(1,11):
    stack.append(i)