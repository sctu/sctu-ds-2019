stack = []
for i in "Hello,World!":
    stack.append(i)

p = []
while len(stack) is not 0:
    p.append((stack.pop()))

a=(''.join(p))
print(a)
