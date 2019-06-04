#编程实现括号匹配
stack=[]
LEFT=['{','[','(']
#依次遍历每一个字符
for i in "{[()]}":
    #如果当前字符是左括号，压栈
    if i in LEFT:
        print(i)
        stack.append(i)
    #如果当前字符是右括号，
    if i in RIGHT:
        #print(i)
    left_parenthese = stack.pop()
