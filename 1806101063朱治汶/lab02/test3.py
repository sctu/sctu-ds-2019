b='abcdcba'
stack = []
for i in b:
    stack.append(i)


p = []
while len(stack) is not 0:
    p.append((stack.pop()))

a=''.join(p)
if a==b:
    print(True)
else:
    print(False)



