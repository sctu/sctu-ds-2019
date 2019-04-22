a="abcdcba"
stack=[]
for i in a:
    stack.append(i)
b=[]
while len(stack) is not 0:
    b.append((stack.pop()))
c=''.join(b)
if c==a:
    print(True)
else:
    print(False)
