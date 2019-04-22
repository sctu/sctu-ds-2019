stack = []

for i in 'hello,World!':
    stack.append(i)  #压栈

while len(stack) != 0:
    a = stack.pop()   #出栈
    print(a)