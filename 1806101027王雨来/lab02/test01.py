#倒序打印
stack = []

for i in 'Hello,World!':
    stack.append(i)

result = []
while len(stack) != 0:
    result.append(stack.pop())
print("".join(result))