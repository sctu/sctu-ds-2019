stack = []
a = ['{', '[', '(']
b = ['}', ']', ')']
for i in '{[()]}':
    if i in a:
        stack.append(i)
    if i in b:
        a_parentheses = stack.pop()
        a_index = a.index(a_parentheses)
        b_index =b.index(i)
        if a_index != b_index:
            print('false')
            break
if len(stack) is 0:
    print('true')
else:
    print('flase')
