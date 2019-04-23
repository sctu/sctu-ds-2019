#括号匹配问题

#针对每一个字符进行处理
'''
stack = []
for i in '{[()]}':
    if i =='(' or i=='[' or i=='{'
    stack.append(i)

'''
#如果左括号，入栈；右括号，进行匹配;a.index()可以获取元素下标
#当所有的字符都处理完成后，判断栈是否为空

#a = input("输入括号进行匹配")
left = {"(","[","{"}
right = {")","]","}"}

    stack = []
    for i in expr:
        if i is left:
            stack.append(i)
        elif i in right:
            stack.pop()
        return not stack
result = match('[(){()}]')
print(result)

