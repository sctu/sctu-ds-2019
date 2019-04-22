str = 'abcdcba'
stack = []
for i in str:
    stack.append(i)

stack2 = []
while len(stack) is not 0:
    stack2.append((stack.pop()))

a = ''.join(stack2)
if a == str:
    print(True)
else:
    print(False)