stack= []
LEFT= ['{', '[', '(']
RIGHT= ['}', ']', ')']


for i in '{[()]}':
    if i in LEFT:
        stack.append(i)
    if i in RIGHT:
        left_parentheses=stack.pop()
        if LEFT.index(left_parentheses) \
                != RIGHT.index(i):
            print('不匹配')
            break
if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')
