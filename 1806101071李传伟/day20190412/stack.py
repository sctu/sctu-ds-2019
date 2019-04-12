stack=[]
#压栈
#stack.append(1)
#stack.append(2)
#stack.append(3)
for i in range(1,11):
    stack.append(i)#消除重复3
#for i in "hello":
    #print(i)得到一个又一个的hello中的函数字母

#alt=1 显示屏幕
#ctrl+d 复制一行
#ctrl+x 删除一行
#a=stack.pop(i)#出栈
#print(a)
#当栈不为空的时候一直pop()
while len(stack) is not 0:
    a=stack.pop()
    print(a)
