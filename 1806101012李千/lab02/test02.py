#{[()]}

str="{[()]}"

stack= []

#1.依此遍历每一个字符

for ch in str:
    print(ch)
#2.如果是左括号，入栈
if ch is '（' or \
   ch is '[' or \
   ch is '{':

    stack.append(ch)

#3.如果是右括号，出栈并且；与当前左括号进行匹配
if ch==')' and stack[-1]=='(':
    stack.pop(ch)
elif ch==']' and stack[-1]=='[':
    stack.pop(ch)

#  如果不匹配，return false，如果匹配则继

#当所有字符都处理完成后，栈不为空，返回false，如果匹配则继续。
if len(stack)==0:
    print("匹配完成")
else:
    print("匹配失败")


#当所有字符都处理完后