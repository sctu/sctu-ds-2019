# 编程实现括号匹配

stack=[]
LEFT = ['{','[','(']
RIGHT = ['}',']',')']

# 依次遍历每一个字符
for i in '{[（）]}':
    # 如果当前字符是左括号，压栈
    if i in LEFT
        # print(i)
        stack.append(i)

    # 如果当前字符是右括号
    if i in RIGHT:
        # print(i)
        left_parenthese = stack.pop()

        left_index = LEFT.index(left_parenthese)
        right_index = RIGHT.index(i)

        if left_index != right_index:
            print('不匹配')
            break

# 当所有字符都处理完成以后
if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')
