stack = []
LEFT = ['(', '[', '{']
RIGHT = [')', ']', '}']

#针对每个字符进行处理
for i in '{[()]}':
#如果是左括号则入栈
    if i in LEFT:
        stack.append(i)
#如果是右括号则进行匹配
    if i in RIGHT:
        left = stack.pop()

        if len(stack) == 0:
            print('不匹配')
            break

        if LEFT.index(left) != RIGHT.index(i):
            print('不匹配')
            break

#当所有的字符都处理完后，判断栈是否为空
if len(stack) == 0:
    print('匹配')
else:
    print('不匹配')



