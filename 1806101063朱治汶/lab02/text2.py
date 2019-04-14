str = '{[()]}'
left ='{[('
right = '}])'

stack = []
for ch in str:
    if ch is '{'or\
       ch is '['or\
       ch is '(':
        stack.append(ch)
    elif ch is '}'or\
         ch is '}'or\
         ch is ')':
        stack.pop()
if stack:
    print(True)
else:
    print(False)




