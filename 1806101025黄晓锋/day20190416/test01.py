#字符串反转

#输入hello，world

#输出dlrow，olleh

stack=[]
X=input('请输入需要反转的语句：')

#1。将每一个字符压栈
for i in X:
    stack.append(i)

#2.出栈，直到栈为空，并打印每一个字符
while len(stack)!=0:
    a=stack.pop()
    print(a,end='')