#括号匹配
stack=[]
stack1=['{[()]}']
Left=['{','[','(']
Right=['}',']',')']

#1.对每一个字符进行处理
for i in stack1:

#2.如果是左括号，则入栈
    if i in Left:
        stack.append(i)

#3.如果是右括号，则进行比较
    elif i in Right:
#如果匹配成功，返回True
        left=stack.pop()
#如果匹配失败，返回False
        if Left.index(Left)!=Right.index() or len(stack)==0:
            print('Flse')
            break

#4.当所有的字符都处理完后，判断栈是否为空。
if len(stack)==0:
    print('True')
else:
    print('False')