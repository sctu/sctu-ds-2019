stack=[]
left=['{','[',')']
right=['}',']',')']
# 依次遍历每个字符
for i in '{[()]}':
# 如果当前字符是左括号    压栈
    if i in left:
        # print(i)
        stack.append(i)
# 如果当前字符是右括号    出栈
    if i in right:
        # print(i)    left_parentheses左括号  break终止整个循环
        left_parentheses=stack.pop()

        left_index=left.index( left_parentheses)
        right_index=right.index(i)

        if  left_index  != right_index:
            print('不匹配')
            break


# 当所有字符都处理完成后
if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')