str='abcdcba'
stack = []
for i in str:
    stack.append(i)


px= []
while len(stack) is not 0:
    px.append((stack.pop()))

a=''.join(px)
if a==str:
    print(True)
else:
    print(False)



