#{[()]

str='{[()]}'
stack=[]
zuobian=['{' '[' '(']
youbian=['}' ']' ')']
#1.依次遍历每一个字符,针对每一个字符进行处理
for i in str:
    print(i)

    if i in zuobian:
        stack.append(i)
    elif i in youbian:
        stack.append(i)
    if stack and stack[-1] == str[i]:
        stack.pop()
    else:
        stack.append(i)



#3.如果是右括号
#  出栈并且与当前左括号进行匹配
#  如果匹配则继续
#4.当所有字符都处理完成后
#  栈不为空，返回False
#  如果栈为空，则return True





