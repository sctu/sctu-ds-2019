# 编程实现括号匹配。
#
# 输入：{[()]}
#
# 输出：True
#push every "left" into the stack
str = "({[)}]"
stack = []
left = ['(','{','[']
right = [')','}',']']
for ch in str:
    if ch in left:
        stack.append(ch)
    if ch in right:
        left_parentheses = stack.pop()
        left_index = left.index(left_parentheses)
        right_index = right.index(ch)

        if left_index != right_index:
            print("不匹配")
            break
if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')




