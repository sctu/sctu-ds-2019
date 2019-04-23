# 2、编程实现括号匹配。

# 输入：{[()]}

# 输出：True
stack = []
LEFT = ['{','[','(']
RIGHT = ['}',']',')']
for i in '{[()]}':
    if i in LEFT:
        stack.append(i)
    if i in RIGHT:
        left_parentheses = stack.pop()
        left_index = LEFT.index(left_parentheses)
        right_index = RIGHT.index(i)

    if left_index != right_index:
        print('不匹配')
        break
if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')
