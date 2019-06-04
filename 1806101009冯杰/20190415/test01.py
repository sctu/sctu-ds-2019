stack = []
for i in 'hello,world!':
    stack.append(i)
result = []
while len(stack) !=0:
     result.append(stack.pop())
print("".join(result))