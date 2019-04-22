#编程实现括号匹配
stack = []
left = ['{','[','(']
right = ['}',']',')']
#依次遍历每一个字符
for i in '{[()]}'
    #如果是左括号，压栈
for i in left:
    #print(i)
    stack.append(i)
#如果当前符号是右括号，
for i in right:
    #print(i)
    left_parentheses = stack.pop()
    left_index = left.index(left_parentheses)
    right_index = right.index(i)
    if left_index != right_index:
        print('不匹配')
#当所有字符都处理完后
if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')