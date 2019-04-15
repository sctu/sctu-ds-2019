stack=[]
LEFT=['{','[','(']
RIGHT=['}',']',')']
for i in'{[()]}':
    if i in LEFT:
        stack.append(i)
    if i in RIGHT:
       left_parentheses=stack.pop()
       left_index=LEFT.index(left_parentheses)
       right_index=RIGHT.index(i)
       if left_index!= right_index:
            print('False')
            break
if len(stack) is 0:
    print('True')
else:
    print('False')

