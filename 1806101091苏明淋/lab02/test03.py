stack = []
queue = []
for i in 'abcdcba':
    stack.append(i)

while len(stack) != 0:
    queue.append(stack.pop())

for i in 'abcdcba':
    stack.append(i)

if stack == queue:
    print("True")
else:
    print("False")