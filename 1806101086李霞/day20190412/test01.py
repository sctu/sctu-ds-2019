stack = []

for i in 'Hello,World!':
    stack.append(i)

result = []

while len(stack) is not 0:
    result.append(stack.pop())
    print(result.pop(),end = "")
