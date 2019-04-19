#编程实现字符串反转
#1.将每一个字符压栈

stack=[]
for i in 'hello,world!':
    stack.append(i)

#2.出栈直到栈为空为止，并且打印每一个字符
while len(stack) !=0:
    a=stack.pop()
    print(a)
