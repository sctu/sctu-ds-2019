#lab2、编程实现括号匹配。输入：{[()]} 输出：True

stack = []
LEFT = ['{']
#1.针对每一个字符进行处理
for i in '{[()]}':
#2.如果是左括号，则入栈
    if i in LEFT:
    # print(i)        KLP
        stack.append(i)
#3.如果是右括号，则进行匹配
    if i in RIGHT:
        #print(i)
        left_parentheses = stack.pop()
        left_index = LEFT .index(left_parent)
        right_index=RIGHT_index(i)

        if left_index !=right_index:
            print('不匹配')
            break
#4.当所有的字符都处理完成后，
if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')
#判断栈是否为空






