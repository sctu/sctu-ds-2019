#编程实现括号匹配
stack=[]


left=['{','[','(']
right=['}',']',')']
#如果当前字符是左括号，则入栈
for i in '{[()]}':
    if i=='{' or i=='[' or i=='(':
        stack.append(i)
#如果当前字符是右括号，则出栈一个字符进行匹配
    if i=='}' or i==']' or i==')':
        left_paretheses=stack.pop()
        if left.index(left_paretheses)!=right.index(i):
            print("匹配失败")
            break


#当所有的字符处理完后，判断栈是否为空
if len(stack=0):
    print("匹配成功")
else:
    print("匹配失败")
#匹配
#a=['{','[','(']
#b=['}',']',')']
#print(a.index('['))
#print(a.index('')==b.index(''))