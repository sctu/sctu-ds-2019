# 编程实现括号匹配。
# 输入：{[()]}
# 输出：True

stack = []
LEFT = ['{', '[', '(']
RIGHT = ['}', ']', ')']
# 依次遍历每一个字符
for i in '{[()]}':
    # 如果当前是左括号，压栈
    if i in LEFT:
        # print(i)
        stack.append(i)
    # 如果当前字符是右括号，
    if i in RIGHT:
        # print(i)
        left_parentheses = stack.pop()
        # 当前左括号下标
        left_index = LEFT.index(left_parentheses)
        # 当前右括号下标
        right_index = RIGHT.index(i)

        if left_index != right_index:
            print('不匹配')
            break
# 当所有字符都处理完成后
if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')