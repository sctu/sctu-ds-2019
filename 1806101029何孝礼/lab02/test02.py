stack=[]
Left=['{','[','(']
Right=['}',']',')']
for i in '{{()}}':
    if i in Left:
        stack.append(i)
    if i in Right:
        left_parentheses=stack.pop()

        left_index=Left.index(left_parentheses)
        right_index=Right.index(i)

        if left_index !=right_index:
            print('')
            break

if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')
