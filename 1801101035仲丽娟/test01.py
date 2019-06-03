stack = []
for i in'Hello,World!':
    stack.append(i)
result = []
while len(stack) != 0:
    print(stack.pop())
    print("".join(result))


