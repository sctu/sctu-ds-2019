#{[()]
def check
str='{[()]}'
stack=[]
zuobian='{[('
youbian='}])'
#1.依次遍历每一个字符
for i in str:
    print(i)

#2.如果是左括号，入栈
    if i in zuobian:
        stack.append(i)
    elif i in youbian:
        stack.append(i)
    if stack and stack[-1] == str[i]:
        stack.pop()
    else:


#3.如果是右括号
#  出栈并且与当前左括号进行匹配
#  如果匹配则继续
#4.当所有字符都处理完成后
#  栈不为空，返回False
#  如果栈为空，则return True




