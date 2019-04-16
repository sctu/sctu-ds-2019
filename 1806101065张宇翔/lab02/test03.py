X='abcdcba'
stack = []
for i in X:
    stack.append(i)
Y = []
while len(stack) is not 0:
    Y.append((stack.pop()))

Z=''.join(Y)
if X==Y:
    print(True)
else:
    print(False)