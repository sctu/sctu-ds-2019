str='{[()]}'
stack=[]
left=['[','{','(']
right=[']','}',')']
for i in str:
    if i in left:
        stack.append(i)

    elif i in right:


        if i in right:
            stack.pop()
        else:
            print("False")
            break

if len(stack)!=0:
    print("False")
else:
    print("True")

#1. 依次遍历每个字符
#2. 如果是左括号，入栈
#3. 如果是右括号，出栈并且与当前左括号进行匹配
#如果不匹配，return False
#如果匹配则继续
#4 当所有字符处理完成后，栈不为空，返回False

