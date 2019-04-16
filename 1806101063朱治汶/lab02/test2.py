str = input('请输入：')
left ='{[('
right = '}])'

stack = []
for ch in str:
    if ch is '{'or\
       ch is '['or\
       ch is '(':
        stack.append(ch)

    elif ch is '}'or\
         ch is ']'or\
         ch is ')':
        stack.pop()

if len(stack)==0:
    print(True)
else:
    print(False)




