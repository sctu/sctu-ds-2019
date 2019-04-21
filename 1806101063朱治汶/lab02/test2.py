str = input('请输入：')
left ='{[('
right = '}])'

stack = []
for ch in str:
    if ch is '{'or\
       ch is '['or\
       ch is '(':
        stack.append(ch)
    elif len(stack)==0:
        stack.append(1)
        break
    elif ch is '}':
        if stack[-1]=="{":
            stack.pop()
        else:break
    elif ch is ']':
        if stack[-1] == "[":
            stack.pop()
        else:break
    elif ch is ')':
        if stack[-1] == "(":
            stack.pop()
        else:
            break

if len(stack)==0:
    print(True)
else:
    print(False)




