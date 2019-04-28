str='{[()]}'
left='{[('
right='}])'
stack=[]
for ch in str:
    print(ch)
    if ch is '(' or \
        ch is '[' or \
        ch is '{':
        stack.append(ch)
    print()