#依次遍历每一个字符
stack=[]
LEFT=['{','[','(']
RIGHT=['{','[','(']

for i in '[()]':
    #如果当前字符是左括号压栈
    if i in LEFT:
        #print(i)
        stack.append(i)

    #若果当前字符是右括号，
    if i in RIGHT:
        #print(i)
        left_parentheses = stack.pop()
    #当前左括号下标
        left_index=LEFT.index(left_parentheses)
    #当前右括号下标
    right_index=RIGHT.index(i)

    if left_index !=right_index:
        print('不匹配')
        break