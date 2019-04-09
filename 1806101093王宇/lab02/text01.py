stack = []

for i in "hello world":
    stack.append(i)

while len(stack) is not 0:
    print(stack.pop(),end="")
