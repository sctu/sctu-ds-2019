stack=[]
str='{[()]}'
Left='{[('
Right='}])'

#进行便利.
for ch in str:
    print(ch)

# 若果是右括号，则入栈.
    if ch is in 'Left':
        stack.append(ch)

#如果是右括号，则与与当前左括号比较，若匹配，则继续，不匹配，则return False.
    if ch is in 'Right':
        stack.append(ch)
        
